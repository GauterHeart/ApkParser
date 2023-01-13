from app.controller.v1.schema import DownloadSchema
from app.core.downloader import Downloader


class DownloadHandler:
    def __init__(self, downloader: Downloader) -> None:
        self.__downloader = downloader

    async def execute(self, spell: DownloadSchema) -> None:
        for s in spell.link:
            self.__downloader.download(url=s)
