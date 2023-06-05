from fastapi import FastAPI
#from routes.user import user
from dotenv import load_dotenv
load_dotenv()
from routes.news import news
app = FastAPI()
#app.include_router(user)
app.include_router(news)