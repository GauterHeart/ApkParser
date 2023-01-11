from typing import List

from pydantic import HttpUrl

from app.model import LinkModel
from app.pkg.database import Postgresql


class LinkCRUD:
    def __init__(self, cursor: Postgresql):
        self.__cursor = cursor

    async def create(self, link: HttpUrl) -> None:
        query = """
            insert into link(link) values($1);
        """
        await self.__cursor.execute(query, link)

    async def fetch(self, link: str) -> List[LinkModel]:
        query = """
            select * from link where link like $1;
        """
        effect = await self.__cursor.fetch(query, f"%{link}%")
        return [LinkModel(**e) for e in effect]

    async def batch_create(self, link: List[HttpUrl]) -> None:
        ...