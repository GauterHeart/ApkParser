from typing import List

from fastapi import APIRouter

from app.controller.v1.handler import LinkHandler
from app.controller.v1.schema import LinkCreateSchema, LinkFetchSchema
from app.model import LinkModel
from app.pkg.arch import HttpControllerABC


class LinkHttpController(HttpControllerABC):
    router = APIRouter(prefix="/link", tags=["Link"])

    def __init__(self, handler: LinkHandler) -> None:
        self.__handler = handler
        self._init_router()

    def _init_router(self) -> None:
        self.router.add_api_route(
            path="/create", endpoint=self.__create, methods=["POST"]
        )
        self.router.add_api_route(
            path="/fetch", endpoint=self.__fetch, methods=["POST"]
        )

    async def __create(self, spell: LinkCreateSchema) -> None:
        await self.__handler.create(spell=spell)

    async def __fetch(self, spell: LinkFetchSchema) -> List[LinkModel]:
        effect = await self.__handler.fetch(spell=spell)
        return effect
