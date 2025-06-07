from pydantic import BaseModel

class PostBase(BaseModel):
    content:str
    title:str
    id:int

    class Config:
        from_attributes = True 

class CreatePost(PostBase):
    class Config:
        from_attributes = True 