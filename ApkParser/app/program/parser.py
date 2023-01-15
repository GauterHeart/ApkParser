from app.core.parser import Parser
from app.pkg.arch import AppABC
import asyncio

from .app import BaseApp


class ParserV1App(BaseApp, AppABC):
    name = "parser_v1"

    def __init_app(self) -> Parser:
        return Parser(
            crud_p=self._crud.init_postgres_crud(),
            url=self._config.APK_URL,
            link_len=self._config.LINK_LEN,
            rabbit=self._rabbit_publisher,
            queue_download=self._config.RABBIT_QUEUE_DOWNLOAD,
        )

    def run(self) -> None:
        asyncio.run(self.__init_app().run())
