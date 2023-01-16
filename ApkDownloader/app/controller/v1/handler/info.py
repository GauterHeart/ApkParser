from typing import List

from app.controller.v1.schema import InfoFetchSchema
from app.crud import PostgresCRUD
from app.model import DownloadModel


class InfoHandler:
    def __init__(self, crud_p: PostgresCRUD) -> None:
        self.__crud_p = crud_p

    async def fetch(self, spell: InfoFetchSchema) -> List[DownloadModel]:
        effect = await self.__crud_p.download.fetch(link=spell.link)
        return effect
