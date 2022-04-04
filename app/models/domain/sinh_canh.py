from pydantic import BaseModel, Field


class SinhCanhName(BaseModel):
    name: str = Field(alias='name')