from datetime import datetime

from pydantic import BaseModel, Field


class PostBase(BaseModel):
    title: str
    content: str
    publication_date: datetime = Field(default_factory=datetime.now)


    class Config:
        orm_mode = True


class PostPartialUpdate(PostBase):
    title: str | None = None
    content: str | None = None


class PostCreate(PostBase):
    pass


class PostRead(PostBase):
    id: int
