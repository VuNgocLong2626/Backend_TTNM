from pydantic import BaseModel, Field


class ImagePath(BaseModel):
    name: str = Field(alias='name')