import requests
from fastapi import APIRouter
news = APIRouter()
import requests
import os
api_key = os.environ.get("API_key")

import uuid
from pydantic import BaseModel, Field
from pymongo import MongoClient
CONNECTION_STRING = 'mongodb://localhost:27017'
client = MongoClient(CONNECTION_STRING)
db = client['news_artikel']
collection = db['news']

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

def create_news():
    url = ('https://newsapi.org/v2/everything?'
           'q=Apple&'
           'from=2023-06-04&'
           'sortBy=popularity&'
           f'apiKey={api_key}')

    response = requests.get(url)
    data = response.json()
    print(data)

    articl = []
    count=0
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
        count+=1
        if count>=5:
           break

        print(articl)
        values =[[
            description,
            title,
            urlToImage,
            url,
            author,
        ]]
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



@news.get("/news")
def get_news():
   articles = create_news()
   print(articles)
   return articles

