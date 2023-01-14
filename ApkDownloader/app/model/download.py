from datetime import datetime

from pydantic import BaseModel, Field, HttpUrl


class DownloadModel(BaseModel):
    url: HttpUrl
    filename: str = Field(..., max_length=512)
    archive: str = Field(..., max_length=512)
    file_size: int
    archive_size: int
    date_create: datetime
