from pydantic import Field, HttpUrl

from app.core.schema import BaseSchema


class LinkCreateSchema(BaseSchema):
    link: HttpUrl


class LinkFetchSchema(BaseSchema):
    link: str = Field(..., max_length=2048)
