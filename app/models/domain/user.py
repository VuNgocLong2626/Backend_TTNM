from pydantic import BaseModel, Field


class UserTk(BaseModel):
    tk: str = Field(alias='tk')


class UserMk(BaseModel):
    mk: str = Field(alias='mk')


class UserHten(BaseModel):
    hten: str = Field(alias='hten')