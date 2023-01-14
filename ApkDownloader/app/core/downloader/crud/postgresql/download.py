from app.pkg.database import SyncPostgresql


class DownloadCRUD:
    def __init__(self, cursor: SyncPostgresql) -> None:
        self.__cursor = cursor

    def create(
        self, url: str, filename: str, archive: str, file_size: int, archive_size: int
    ) -> None:
        query = """
            insert into download(
                    url,
                    filename,
                    archive,
                    file_size,
                    archive_size)
            values(
                '%(url)s',
                '%(filename)s',
                '%(archive)s',
                %(file_size)s,
                %(archive_size)s);
        """
        self.__cursor.execute(
            query=query,
            arg={
                "url": url,
                "filename": filename,
                "archive": archive,
                "file_size": file_size,
                "archive_size": archive_size,
            },
        )
