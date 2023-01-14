from typing import List

from pydantic import BaseModel, HttpUrl


class ParserDownloadModel(BaseModel):
    link: List[HttpUrl]
