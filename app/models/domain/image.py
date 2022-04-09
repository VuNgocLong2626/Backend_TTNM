from pydantic import BaseModel, Field


class ImagePath(BaseModel):
    path: str = Field(alias='path')