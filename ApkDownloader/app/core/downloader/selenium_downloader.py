from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from .base import Downloader


class SeleniumDownloader(Downloader):
    def __init__(self, path: str) -> None:
        self.__path = path
        self.__driver = webdriver.Firefox(options=self.__init_driver_options())

    def __init_driver_options(self) -> Options:
        options = Options()
        options.add_argument("--headless")
        options.set_preference("browser.download.folderList", 2)
        options.set_preference("browser.download.dir", self.__path)
        return options

    def download(self, url: str) -> None:
        self.__driver.get(url=url)
