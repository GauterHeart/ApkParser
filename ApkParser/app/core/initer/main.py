import asyncio

from loguru import logger

from app.pkg.database import Redis, SyncPostgresql

from .exception import (
    SystemHealthPostgresqlConnectionException,
    SystemHealthRedisConnectionException,
)


class IniterService:

    cursor_p: SyncPostgresql
    cursor_r: Redis

    @classmethod
    def health_connection_postgresql(cls) -> None:
        query = """select sum(1+2);"""
        try:
            cls.cursor_p.get(query=query, arg={})
        except Exception:
            raise SystemHealthPostgresqlConnectionException()

        logger.success("Postgresql connection OK")

    @classmethod
    def health_connection_redis(cls) -> None:
        try:
            asyncio.run(cls.cursor_r.set(name="test", value="test", expire=5))
        except Exception:
            raise SystemHealthRedisConnectionException()

        logger.success("Redis connection OK")
