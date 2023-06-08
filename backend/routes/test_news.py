from fastapi.testclient import TestClient
from fastapi import APIRouter
from routes.news import news
news = APIRouter()
client = TestClient(news)
def test_news_get():
    response = client.get("/news")
    assert response.status_code ==200
    assert result = news
    assert response.json()=={}