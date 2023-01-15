from pydantic import Field

from app.core.schema import BaseAuthSchema


class FileFetchSchema(BaseAuthSchema):
    link: str = Field(..., max_length=2048)
