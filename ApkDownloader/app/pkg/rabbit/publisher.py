import aio_pika
from aio_pika.abc import AbstractRobustConnection
from aio_pika.pool import Pool
from pydantic import BaseModel


class RabbitPublisher:

    __connection_pool: Pool
    __channel_pool: Pool

    def __init__(self, dsn: str):
        self.__dsn = dsn

    async def __get_connection(self) -> AbstractRobustConnection:
        return await aio_pika.connect_robust(self.__dsn)

    async def __get_channel(self) -> aio_pika.Channel:
        async with self.__connection_pool.acquire() as connection:
            return await connection.channel()

    async def __make_connection(self) -> None:
        self.__connection_pool = Pool(self.__get_connection, max_size=2)
        self.__channel_pool: Pool = Pool(self.__get_channel, max_size=10)

    async def init_connection(self) -> None:
        await self.__make_connection()

    async def publish(self, msg: BaseModel, queue: str) -> None:
        async with self.__channel_pool.acquire() as channel:
            await channel.default_exchange.publish(
                aio_pika.Message(msg.json().encode("utf-8")),
                queue,
            ),
