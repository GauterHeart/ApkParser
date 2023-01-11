from typing import List

from app.controller.v1.schema import LinkCreateSchema, LinkFetchSchema
from app.crud import PostgresCRUD
from app.model import LinkModel


class LinkHandler:
    def __init__(self, crud_p: PostgresCRUD) -> None:
        self.__crud_p = crud_p

    async def create(self, spell: LinkCreateSchema) -> None:
        await self.__crud_p.link.create(link=spell.link)

    async def fetch(self, spell: LinkFetchSchema) -> List[LinkModel]:
        effect = await self.__crud_p.link.fetch(link=spell.link)
        return effect
