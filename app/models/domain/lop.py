from pydantic import BaseModel, Field


class LopName(BaseModel):
    name: str = Field(alias='name')