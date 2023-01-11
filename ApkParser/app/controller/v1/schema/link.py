from pydantic import BaseModel, Field, HttpUrl


class LinkCreateSchema(BaseModel):
    link: HttpUrl


class LinkFetchSchema(BaseModel):
    link: str = Field(..., max_length=2048)
