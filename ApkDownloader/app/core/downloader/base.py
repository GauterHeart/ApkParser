from abc import ABC, abstractmethod


class Downloader(ABC):
    @abstractmethod
    def download(self, url: str) -> None:
        ...
