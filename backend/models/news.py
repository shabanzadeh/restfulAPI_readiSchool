from pydantic import BaseModel

class News(BaseModel):
    description: str
    title:str
    url:str
    urlToImage:str
    author:str