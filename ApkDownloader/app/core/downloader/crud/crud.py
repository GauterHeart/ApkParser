from dataclasses import dataclass

from app.pkg.database import SyncPostgresql

from .postgresql import DownloadCRUD


@dataclass(frozen=True)
class PostgresDownloaderCRUD:
    download: DownloadCRUD


class FactoryDownloaderCrud:
    def __init__(self, postgres_cursor: SyncPostgresql):
        self.__postgres_cursor = postgres_cursor

    def init_postgres_crud(self) -> PostgresDownloaderCRUD:
        return PostgresDownloaderCRUD(
            download=DownloadCRUD(cursor=self.__postgres_cursor),
        )
