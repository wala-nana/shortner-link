from pydantic import BaseModel

class Link(BaseModel):
    link_name: str
    link_url: str

    class Config: 
        orm_mode = True


class ShortLink(BaseModel):
    link_url: str

    class Config: 
        orm_mode = True