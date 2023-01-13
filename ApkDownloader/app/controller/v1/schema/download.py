from typing import List

from pydantic import BaseModel, HttpUrl


class DownloadSchema(BaseModel):
    link: List[HttpUrl]
