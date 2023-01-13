import glob
import os

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from app.core.namespace import DownloadNS

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
        files = glob.glob("{}{}".format(DownloadNS.DIR.value, "/*"))
        latest_file = max(files, key=os.path.getctime)
        new_path = latest_file.replace(
            latest_file.split("/")[-1].split(".")[0],
            "{}{}".format(url.split(DownloadNS.BASE_URL.value)[1], ".apk"),
        )
        os.rename(latest_file, new_path)
