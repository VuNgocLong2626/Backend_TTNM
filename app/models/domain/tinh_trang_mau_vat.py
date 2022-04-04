from pydantic import BaseModel, Field


class TinhTrangMauVatName(BaseModel):
    name: str = Field(alias='name')