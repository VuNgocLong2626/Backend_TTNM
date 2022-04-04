from pydantic import BaseModel, Field


class BoName(BaseModel):
    name: str = Field(alias='name')