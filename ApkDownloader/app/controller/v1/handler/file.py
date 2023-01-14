from typing import List

from app.controller.v1.schema import FileFetchSchema
from app.crud import PostgresCRUD
from app.model import DownloadModel


class FileHandler:
    def __init__(self, crud_p: PostgresCRUD) -> None:
        self.__crud_p = crud_p

    async def fetch(self, spell: FileFetchSchema) -> List[DownloadModel]:
        effect = await self.__crud_p.file.fetch(link=spell.link)
        return effect
