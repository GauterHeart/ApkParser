import asyncio
from pprint import pprint
from typing import List

import httpx
from bs4 import BeautifulSoup
from pydantic import HttpUrl

from app.crud import PostgresCRUD


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

    def __init__(self, crud_p: PostgresCRUD, url: HttpUrl, link_len: int) -> None:
        self.__crud_p = crud_p
        self.__url = url
        self.__link_len = link_len

    def run(self) -> None:
        asyncio.run(self.__parser())

    async def _make_request(self, route: str = "") -> httpx.Response:
        print("{}{}".format(self.__url, route))
        async with httpx.AsyncClient() as client:
            effect = await client.post(url="{}{}".format(self.__url, route))
            return effect

    async def _add_base_link(self, page: int) -> List[str]:
        """
        Parse Table Page
        """
        arr: List[str] = []
        effect = await self._make_request(route=f"/uploads/page/{page}/")
        soup = BeautifulSoup(effect.text, "lxml")
        e_1 = soup.select("a[class='downloadLink']")
        for j in e_1:
            arr.append(j["href"])

        return arr

    async def _version_link(self, route: str) -> List[str]:
        """
        Parse version distro
        """
        effect = await self._make_request(route=route)
        soup = BeautifulSoup(effect.text, "lxml")
        href = soup.select("a[class='accent_color']")
        return [h["href"] for h in href if h["href"] != "/faq/"]

    async def _download_link(self, route: str) -> str:
        """
        Get download link
        """
        effect = await self._make_request(route=route)
        soup = BeautifulSoup(effect.text, "lxml")
        href = soup.find("a", {"class": "downloadButton"})
        if href is None:
            return ""

        return href["href"]

    async def __parser(self) -> None:
        page = 1
        arr_download: List[str] = []
        while len(arr_download) < self.__link_len:
            arr_base_link = await self._add_base_link(page=page)
            arr_base_link = arr_base_link
            arr_version_link: List[str] = []
            for a in arr_base_link:
                try:
                    arr = await self._version_link(route=a)
                except httpx.ConnectError:
                    arr.extend([])  # remove(for test)
                    continue

                arr_version_link.extend(arr)

            for a in arr_version_link:
                try:
                    tmp = await self._download_link(route=a)
                except httpx.ConnectError:
                    arr_download.append("")  # remove(for test)
                    continue

                arr_download.append(tmp)

            print("=========")
            pprint(arr_download)
            print("LEN = ", len(arr_download))
            arr_download = list(
                filter(lambda x: x != "" or x != "#downloads", arr_download)
            )
            page += 1

        arr_download = list(map(lambda x: "{}{}".format(self.__url, x), arr_download))
