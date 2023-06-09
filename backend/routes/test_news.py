import unittest
from fastapi.testclient import TestClient
from routes.news import news

class NewsEndpointTestCase(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(news.app)
    def test_get_news(self):
        response = self.client.get("/news")
        self.assertEqual(response.status_code, 200)



if __name__ == "__main__":
    unittest.main()
