from pydantic import BaseModel, Field


class BaseAuthSchema(BaseModel):
    unixtime: str = Field(..., max_length=128)
