from datetime import datetime

from pydantic import BaseModel, HttpUrl


class LinkModel(BaseModel):
    id: int
    link: HttpUrl
    date_create: datetime
