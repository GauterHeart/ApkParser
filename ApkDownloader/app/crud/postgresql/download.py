from typing import List

from app.model import DownloadModel
from app.pkg.database import Postgresql


class DownloadCRUD:
    def __init__(self, cursor: Postgresql) -> None:
        self.__cursor = cursor

    async def fetch(self, link: str) -> List[DownloadModel]:
        query = """
            select * from download where url like $1
            order by date_create desc limit 1000;
        """
        effect = await self.__cursor.fetch(query, f"%{link}%")
        return [DownloadModel(**e) for e in effect]
