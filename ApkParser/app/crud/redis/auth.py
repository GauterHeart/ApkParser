from typing import Optional

from app.pkg.database import Redis


class AuthRedisCRUD:
    def __init__(self, cursor: Redis):
        self.__cursor = cursor

    async def create(self, unixtime: str, request_id: str, expire: int) -> None:
        await self.__cursor.set(name=request_id, value=unixtime, expire=expire)

    async def get(self, request_id: str) -> Optional[str]:
        return await self.__cursor.get(name=request_id)

    async def delete(self, request_id: str) -> None:
        await self.__cursor.delete(name=request_id)
