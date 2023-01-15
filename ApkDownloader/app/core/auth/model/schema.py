from pydantic import BaseModel, Field


class AuthSchema(BaseModel):
    id: str = Field(..., max_length=128)
    unixtime: str = Field(..., max_length=128)
