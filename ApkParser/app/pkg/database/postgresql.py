from contextlib import asynccontextmanager
from typing import Any, AsyncGenerator, List

import asyncpg


class Postgresql:
    def __init__(self, host: str, port: int, user: str, password: str, db: str) -> None:
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db
        self.__pool: asyncpg.Pool | None = None

    @asynccontextmanager
    async def __create_connector(self) -> AsyncGenerator:

        if self.__pool is None:
            self.__pool = await asyncpg.create_pool(
                database=self.db,
                user=self.user,
                port=self.port,
                password=self.password,
                host=self.host,
            )

        async with self.__pool.acquire() as connection:
            yield connection

    async def execute(self, query: str, *args: Any) -> None:
        async with self.__create_connector() as conn:
            async with conn.transaction():
                await conn.execute(query, *args)

    async def executemany(self, query: str, *args: Any) -> None:
        async with self.__create_connector() as conn:
            async with conn.transaction():
                await conn.executemany(query, *args)

    async def fetchrow(self, query: str, *args: Any) -> dict:
        async with self.__create_connector() as conn:
            async with conn.transaction():
                resp = await conn.fetchrow(query, *args)
        return resp

    async def fetch(self, query: str, *args: Any) -> List[dict]:
        async with self.__create_connector() as conn:
            async with conn.transaction():
                resp = await conn.fetch(query, *args)
        return resp
