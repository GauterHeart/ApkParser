from .base import Downloader


class ParseDownloader(Downloader):
    def download(self, url: str) -> None:
        ...
