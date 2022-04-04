from pydantic import BaseModel, Field


class PhanBoName(BaseModel):
    name: str = Field(alias='name')