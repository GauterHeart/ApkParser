from typing import List

from fastapi import APIRouter

from app.controller.v1.handler import FileHandler
from app.controller.v1.schema import FileFetchSchema
from app.model import DownloadModel
from app.pkg.arch import HttpControllerABC


class FileHttpController(HttpControllerABC):
    router = APIRouter(prefix="/file", tags=["File"])

    def __init__(self, handler: FileHandler) -> None:
        self.__handler = handler
        self._init_router()

    def _init_router(self) -> None:
        self.router.add_api_route(
            path="/fetch", endpoint=self.__fetch, methods=["POST"]
        )

    async def __fetch(self, spell: FileFetchSchema) -> List[DownloadModel]:
        effect = await self.__handler.fetch(spell=spell)
        return effect
