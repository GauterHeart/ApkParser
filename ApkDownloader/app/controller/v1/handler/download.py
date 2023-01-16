from app.controller.v1.schema import DownloadSchema
from app.core.downloader import Downloader
from app.core.rabbit.exception import RabbitDownloadException


class DownloadHandler:
    def __init__(self, downloader: Downloader) -> None:
        self.__downloader = downloader

    async def execute(self, spell: DownloadSchema) -> None:
        for s in spell.link:
            try:
                self.__downloader.download(url=s)
            except Exception:
                raise RabbitDownloadException()
