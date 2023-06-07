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

from models.news import News
from config.db import conn
from schemas.news import newsEntity


@news.get("/news")
def get_news():
    url = ('https://newsapi.org/v2/everything?'
           'q=Apple&'
           'from=2023-06-04&'
           'sortBy=popularity&'
           f'apiKey={api_key}')

    response = requests.get(url)
    data = response.json()

    articles = []
    for article in data["articles"]:
        description = article["description"]
        title = article["title"]
        urlToImage = article["urlToImage"]
        url = article["url"]
        author = article["author"]
        articles.append({
            "description": description,
            "title": title,
            "urlToImage": urlToImage,
            "url": url,
            "author": author
        })

    return articles


def storeArtikel(articles):
    news_dataes = get_news()
    client = MongoClient('mongodb://localhost:27017/')
    return newsEntity(conn.local.news.insert_many(articles))



#@user.post('/')
#async def create_users(user:User):
 #   return usersEntity(conn.local.user.insert_one(dict(user)))

