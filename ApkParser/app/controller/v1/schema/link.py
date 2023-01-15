from pydantic import Field, HttpUrl

from app.core.schema import BaseAuthSchema


class LinkCreateSchema(BaseAuthSchema):
    link: HttpUrl


class LinkFetchSchema(BaseAuthSchema):
    link: str = Field(..., max_length=2048)
