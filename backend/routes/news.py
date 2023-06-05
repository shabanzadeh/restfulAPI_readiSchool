import requests
from fastapi import APIRouter
news = APIRouter()
import requests
from fastapi import APIRouter
import os
api_key = os.environ.get("API_key")
news = APIRouter()

@news.get("/news")
def get_news():
    url = ('https://newsapi.org/v2/everything?'
           'q=Apple&'
           'from=2023-06-04&'
           'sortBy=popularity&'
           f'apiKey={api_key}')

    response = requests.get(url)
    return response.json()
