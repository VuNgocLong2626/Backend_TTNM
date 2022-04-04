from pydantic import BaseModel, Field


class TinhTrangBaoTonName(BaseModel):
    name: str = Field(alias='name')