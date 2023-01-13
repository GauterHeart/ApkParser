from abc import ABC


class Downloader(ABC):
    def download(self, url: str) -> None:
        ...
