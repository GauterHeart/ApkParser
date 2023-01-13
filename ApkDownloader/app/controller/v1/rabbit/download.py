from app.controller.v1.handler import DownloadHandler
from app.controller.v1.schema import DownloadSchema
from app.core.rabbit import RabbitStatusHandler
from app.pkg.rabbit.consumer import RabbitConsumer


class DownloadSeleniumRabbitController(RabbitConsumer):
    def __init__(
        self,
        queue_name: str,
        username: str,
        password: str,
        host: str,
        port: int,
        handler: DownloadHandler,
        status_handler: RabbitStatusHandler,
    ) -> None:
        super().__init__(
            queue_name=queue_name,
            username=username,
            password=password,
            host=host,
            port=port,
            status_handler=status_handler,
        )
        self.__handler = handler

    async def run(self) -> None:
        await self._broker(
            func=self.__handler.selenium,
            model=DownloadSchema,
        )
