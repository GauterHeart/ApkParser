from aio_pika.abc import AbstractMessage

from app.pkg.rabbit import RabbitStatusHandlerABC
from app.pkg.rabbit.exception import BaseRabbitException


class RabbitStatusHandler(RabbitStatusHandlerABC):
    async def func_200(self, msg: AbstractMessage) -> None:
        ...

    async def func_400(
        self, msg: AbstractMessage, exception: BaseRabbitException
    ) -> None:
        ...

    async def func_500(
        self, msg: AbstractMessage, exception: BaseRabbitException
    ) -> None:
        ...
