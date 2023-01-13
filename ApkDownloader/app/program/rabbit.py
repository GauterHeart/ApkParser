import asyncio
import os

from app.controller.v1.handler import DownloadHandler
from app.controller.v1.rabbit import (
    DownloadParseRabbitController,
    DownloadSeleniumRabbitController,
)
from app.core.downloader import ParseDownloader, SeleniumDownloader
from app.core.namespace import DownloadNS
from app.pkg.arch import AppABC
from app.program.app import BaseApp


class RabbitDownloadSeleniumV1App(BaseApp, AppABC):
    name = "rabbit_selenium_v1"

    def __init_rabbit(self) -> DownloadSeleniumRabbitController:
        return DownloadSeleniumRabbitController(
            host=self._config.RABBIT_HOST,
            port=self._config.RABBIT_PORT,
            username=self._config.RABBIT_USER,
            password=self._config.RABBIT_PASSWORD,
            queue_name=self._config.RABBIT_QUEUE_DOWNLOAD_SELENIUM,
            handler=DownloadHandler(
                downloader=SeleniumDownloader(
                    path="{}{}".format(os.path.abspath("./"), DownloadNS.DIR.value)
                )
            ),
            status_handler=self._rabbit_status_handler,
        )

    def run(self) -> None:
        asyncio.run(self.__init_rabbit().run())


class RabbitDownloadParseV1App(BaseApp, AppABC):
    name = "rabbit_parse_v1"

    def __init_rabbit(self) -> DownloadParseRabbitController:
        return DownloadParseRabbitController(
            host=self._config.RABBIT_HOST,
            port=self._config.RABBIT_PORT,
            username=self._config.RABBIT_USER,
            password=self._config.RABBIT_PASSWORD,
            queue_name=self._config.RABBIT_QUEUE_DOWNLOAD_PARSE,
            handler=DownloadHandler(downloader=ParseDownloader()),
            status_handler=self._rabbit_status_handler,
        )

    def run(self) -> None:
        asyncio.run(self.__init_rabbit().run())
