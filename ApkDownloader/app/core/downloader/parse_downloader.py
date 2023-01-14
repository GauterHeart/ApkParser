import os
from uuid import uuid4

import httpx
from bs4 import BeautifulSoup

from app.core.namespace import DownloadNS

from .base import Downloader
from .crud import PostgresDownloaderCRUD


class ParseDownloader(Downloader):
    def __init__(self, url: str, crud_p: PostgresDownloaderCRUD) -> None:
        self.__url = url
        self.__crud_p = crud_p

    def _make_request(self, url: str) -> httpx.Response:
        with httpx.Client() as client:
            effect = client.get(url=url)
            return effect

    def _download_file(self, url: str, filename: str) -> None:
        with open(filename, "wb") as f:
            with httpx.stream("GET", url) as r:
                for chunk in r.iter_bytes():
                    f.write(chunk)

    def download(self, url: str) -> None:
        effect = self._make_request(url=url)
        soup = BeautifulSoup(effect.text, "lxml")
        href = soup.find("div", {"class": "f-sm-50"}).find("a")["href"]
        effect = self._make_request(url="{}{}".format(self.__url, href))
        if effect.status_code != 302:
            return

        name = uuid4().__str__()
        filename = ".{}/{}{}".format(DownloadNS.DIR.value, name, ".apk")
        archive = ".{}/{}{}".format(DownloadNS.DIR.value, name, ".7z")
        self._download_file(
            url=effect.headers["location"],
            filename=filename,
        )
        os.system(f"7z a {archive} {filename}")
        file_size = os.stat(f"{filename}").st_size
        archive_size = os.stat(f"{archive}").st_size

        self.__crud_p.download.create(
            url=url,
            filename=filename,
            archive=archive,
            file_size=file_size,
            archive_size=archive_size,
        )
