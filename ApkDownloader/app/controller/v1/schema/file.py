from pydantic import BaseModel, Field


class FileFetchSchema(BaseModel):
    link: str = Field(..., max_length=2048)
