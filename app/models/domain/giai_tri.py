from pydantic import BaseModel, Field


class GiaTriName(BaseModel):
    name: str = Field(alias='name')