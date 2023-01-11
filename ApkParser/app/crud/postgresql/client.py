from typing import Optional

from app.model import ClientModel
from app.pkg.database import Postgresql


class ClientCRUD:
    def __init__(self, cursor: Postgresql) -> None:
        self.__cursor = cursor

    async def get(self, public_key: str) -> Optional[ClientModel]:
        query = """
            select * from client where public_key = $1;
        """

        effect = await self.__cursor.fetchrow(query, public_key)
        if effect is not None:
            return ClientModel(**effect)

        return effect
