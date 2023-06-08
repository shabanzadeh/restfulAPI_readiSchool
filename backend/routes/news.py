import requests
from fastapi import APIRouter
news = APIRouter()
import requests
from fastapi import APIRouter
import os
from pymongo import MongoClient
conn = MongoClient()
api_key = os.environ.get("API_key")
news = APIRouter()

import uuid
from fastapi import FastAPI, HTTPException, status
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field
from pymongo import MongoClient
CONNECTION_STRING = 'mongodb://localhost:27017'
class News(BaseModel):
  id: str = Field(default_factory=uuid.uuid4, alias="_id")
  description: str
  title:str
  url:str
  urlToImage:str
  author:str
  


# Connect to DB
connection = MongoClient(CONNECTION_STRING)
db = connection.news_artikel

@news.get("/news")
def get_news():
    url = ('https://newsapi.org/v2/everything?'
           'q=Apple&'
           'from=2023-06-04&'
           'sortBy=popularity&'
           f'apiKey={api_key}')

    response = requests.get(url)
    data = response.json()

    articl = []
    for article in data["articles"]:
        description = article["description"]
        title = article["title"]
        urlToImage = article["urlToImage"]
        url = article["url"]
        author = article["author"]
        articl.append({
            "description": description,
            "title": title,
            "urlToImage": urlToImage,
            "url": url,
            "author": author
        })
        print(articl)
        values =[[
            description,
            title,
            urlToImage,
            url,
            author,
        ]]
        client =MongoClient("mongodb://localhost:27017")
        db = client["news_artikel"]
        collection = db["news_artikel"]
        result =[]
        collection.insert_many([{
            "description": value[0],
            "titel": value[1],
            "urlToImage": value[2],
            "url":value[3],
            "autor":value[4],
        }for value in values])
        result.append({description,title,urlToImage,url,author})
        return result







#@user.post('/')
#async def create_users(user:User):
 #   return usersEntity(conn.local.user.insert_one(dict(user)))

