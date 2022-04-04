from pydantic import BaseModel, Field


class HoName(BaseModel):
    name: str = Field(alias='name')