from dataclasses import dataclass

from app.crud.postgresql import ClientCRUD
from app.crud.redis import AuthRedisCRUD
from app.pkg.database import Postgresql, Redis


@dataclass(frozen=True)
class PostgresCRUD:
    client: ClientCRUD


@dataclass(frozen=True)
class RedisCRUD:
    auth: AuthRedisCRUD


class FactoryCrud:
    def __init__(self, postgres_cursor: Postgresql, redis_cursor: Redis):
        self.__postgres_cursor = postgres_cursor
        self.__redis_cursor = redis_cursor

    def init_postgres_crud(self) -> PostgresCRUD:
        return PostgresCRUD(
            client=ClientCRUD(cursor=self.__postgres_cursor),
        )

    def init_redis_crud(self) -> RedisCRUD:
        return RedisCRUD(
            auth=AuthRedisCRUD(cursor=self.__redis_cursor),
        )
