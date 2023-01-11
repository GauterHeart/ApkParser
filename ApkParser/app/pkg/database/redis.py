from contextlib import asynccontextmanager
from typing import Any, Optional

import aioredis

__all__ = ["Redis"]


class Redis:

    __connector: Optional[aioredis.Redis] = None

    def __init__(self, host: str, port: int, user: str, password: str, db: str) -> None:
        self.__host = host
        self.__port = port
        self.__user = user
        self.__password = password
        self.__db = db
        self.__pool = aioredis.ConnectionPool.from_url(
            self.__create_dsn(), max_connections=10
        )

    def __create_dsn(self) -> str:
        return (
            f"redis://{self.__user}:{self.__password}"
            + f"@{self.__host}:{self.__port}/{self.__db}"
        )

    @asynccontextmanager
    async def __create_connector(self) -> Any:
        if self.__connector is None:
            self.__connector = aioredis.Redis(connection_pool=self.__pool)

        yield self.__connector

    async def set(self, name: str, value: str, expire: Optional[int] = None) -> None:
        async with self.__create_connector() as redis:
            async with redis.client() as conn:
                await conn.set(name=name, value=value, ex=expire)

    async def delete(self, name: str) -> None:
        async with self.__create_connector() as redis:
            async with redis.client() as conn:
                await conn.delete(name)

    async def get(self, name: str) -> str:
        async with self.__create_connector() as redis:
            async with redis.client() as conn:
                return await conn.get(name=name)

    async def hgetall(self, name: str) -> dict:
        async with self.__create_connector() as redis:
            async with redis.client() as conn:
                return await conn.hgetall(name=name)

    async def hget(self, name: str, key: str) -> str:
        async with self.__create_connector() as redis:
            async with redis.client() as conn:
                return await conn.hget(name=name, key=key)

    async def hset(self, name: str, key: str, value: str) -> None:
        async with self.__create_connector() as redis:
            async with redis.client() as conn:
                return await conn.hset(name=name, key=key, value=value)
