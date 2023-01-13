from typing import List, Optional, Type

from app.config.config import get_settings
from app.pkg.arch.program import AppABC
from app.program import RabbitDownloadParseV1App, RabbitDownloadSeleniumV1App


class App:

    _config = get_settings()

    def __program(self) -> List[Type[AppABC]]:
        return [RabbitDownloadSeleniumV1App, RabbitDownloadParseV1App]

    def __app(self) -> Optional[AppABC]:
        for p in self.__program():
            if p.name == self._config.PROGRAM:
                return p()
        return None

    def run(self) -> None:
        app = self.__app()

        if app is not None:
            app.run()


app = App()
