from pydantic import Field

from app.core.schema import BaseSchema


class FileFetchSchema(BaseSchema):
    link: str = Field(..., max_length=2048)
