from pydantic import BaseModel

class ShortenerBase(BaseModel):
    redirect_url: str

class Shortener(ShortenerBase):
    id: str

    class Config:
        orm_mode = True

class ShortenerCreate(ShortenerBase):
    pass