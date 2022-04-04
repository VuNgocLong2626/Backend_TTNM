from pydantic import BaseModel, Field


class GioiName(BaseModel):
    name: str = Field(alias='name')