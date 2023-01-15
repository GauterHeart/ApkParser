import asyncio
from contextlib import asynccontextmanager
from typing import AsyncGenerator, AsyncIterator, List

import httpx
from bs4 import BeautifulSoup
from pydantic import HttpUrl

from app.crud import PostgresCRUD
from app.pkg.rabbit import RabbitPublisher

from .model import ParserDownloadModel


async def _inner_iterator(spell: List[str]) -> AsyncIterator[str]:
    for s in spell:
        yield s


class Parser:
    """
    1. div = widget widget_appmanager_recentpostswidget
    2. div = listWidget
    3. div = table-cell
    4. a = downloadLink + href
    5. div = table topmargin variants-table
    6. a = accent_color
    7. a = accent_bg btn btn-flat downloadButton TBL
    """

    def __init__(
        self,
        crud_p: PostgresCRUD,
        rabbit: RabbitPublisher,
        queue_download: str,
        url: HttpUrl,
        link_len: int,
    ) -> None:
        self.__crud_p = crud_p
        self.__url = url
        self.__link_len = link_len
        self.__rabbit = rabbit
        self.__queue_download = queue_download

    async def run(self) -> None:
        await self.__rabbit.init_connection()
        await self.parser()

    async def _make_request(self, route: str = "") -> httpx.Response:
        print("{}{}".format(self.__url, route))
        async with httpx.AsyncClient() as client:
            effect = await client.post(url="{}{}".format(self.__url, route))
            return effect

    @asynccontextmanager
    async def _add_base_link(self, page: int) -> AsyncGenerator[List[str], None]:
        """
        Parse Table Page
        """
        try:
            effect = await self._make_request(route=f"/uploads/page/{page}/")
        except httpx.ConnectError:
            yield []

        soup = BeautifulSoup(effect.text, "lxml")
        e = soup.select("a[class='downloadLink']")
        yield ["/".join(i["href"].split("/")[:-2]) for i in e]

    @asynccontextmanager
    async def _version_link(self, route: str) -> AsyncGenerator[List[str], None]:
        """
        Parse version distro
        """
        try:
            effect = await self._make_request(route=route)
        except httpx.ConnectError:
            yield []

        soup = BeautifulSoup(effect.text, "lxml")
        href = soup.find(id="primary").select("a[class='downloadLink']")
        yield [h["href"] for h in href if h["href"] != "/faq/"]

    async def _download_link(self, route: str) -> str:
        """
        Get download link
        """
        effect = await self._make_request(route=route)
        if effect.status_code == 302:
            return await self._download_link(route=effect.headers["location"])

        soup = BeautifulSoup(effect.text, "lxml")
        href = soup.find("a", {"class": "downloadButton"})
        if href is None:
            return ""

        href = href["href"]
        if href == "#downloads":
            lst = soup.find("div", {"class": "listWidget"}).select(
                "a[class='accent_color']"
            )
            href_lst = [i["href"] for i in lst if i["href"] != "/faq/"]
            return await self._download_link(route=href_lst[0])

        return href

    async def parser(self) -> None:
        # await self.__rabbit.init_connection
        page = 1
        arr_download: List[str] = []
        link_len = self.__link_len
        while link_len > 0:
            async with self._add_base_link(page=page) as arr_base_link:
                async for a in _inner_iterator(arr_base_link):
                    async with self._version_link(route=a) as ctx:
                        async for i in _inner_iterator(ctx):
                            await asyncio.sleep(1)
                            try:
                                tmp = await self._download_link(route=a)
                            except httpx.ConnectError:
                                arr_download.append("")  # remove(for test)
                                continue

                    arr_download.append(tmp)
                    arr_download = list(
                        map(lambda x: "{}{}".format(self.__url, x), arr_download)
                    )

                    async for i in _inner_iterator(arr_download):
                        await self.__crud_p.link.create(link=i)

                    await self.__rabbit.publish(
                        msg=ParserDownloadModel(link=arr_download),
                        queue=self.__queue_download,
                    )
                    link_len -= len(arr_download)
                    del arr_download[:]

            page += 1
