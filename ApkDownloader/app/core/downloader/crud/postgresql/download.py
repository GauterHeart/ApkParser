from app.pkg.database import SyncPostgresql


class DownloadCRUD:
    def __init__(self, cursor: SyncPostgresql) -> None:
        self.__cursor = cursor

    def create(
        self, url: str, filename: str, folder: str, file_size: int, folder_size: int
    ) -> None:
        query = """
            insert into download(
                    url,
                    filename,
                    folder,
                    file_size,
                    folder_size)
            values(
                '%(url)s',
                '%(filename)s',
                '%(folder)s',
                %(file_size)s,
                %(folder_size)s);
        """
        self.__cursor.execute(
            query=query,
            arg={
                "url": url,
                "filename": filename,
                "folder": folder,
                "file_size": file_size,
                "folder_size": folder_size,
            },
        )
