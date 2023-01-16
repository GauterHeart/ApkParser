from typing import List

from fastapi import APIRouter

from app.controller.v1.handler import InfoHandler
from app.controller.v1.schema import InfoFetchSchema
from app.model import DownloadModel
from app.pkg.arch import HttpControllerABC


class InfoHttpController(HttpControllerABC):
    router = APIRouter(prefix="/info", tags=["Info"])

    def __init__(self, handler: InfoHandler) -> None:
        self.__handler = handler
        self._init_router()

    def _init_router(self) -> None:
        self.router.add_api_route(
            path="/fetch", endpoint=self.__fetch, methods=["POST"]
        )

    async def __fetch(self, spell: InfoFetchSchema) -> List[DownloadModel]:
        effect = await self.__handler.fetch(spell=spell)
        return effect
