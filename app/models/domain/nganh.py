from pydantic import BaseModel, Field


class NganhName(BaseModel):
    name: str = Field(alias='name')