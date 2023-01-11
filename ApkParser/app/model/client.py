from pydantic import BaseModel, Field


class ClientModel(BaseModel):
    public_key: str = Field(..., max_length=256)
    private_key: str = Field(..., max_length=512)
