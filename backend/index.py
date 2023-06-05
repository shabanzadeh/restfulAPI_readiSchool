from fastapi import FastAPI
#from routes.user import user
from routes.news import news
from dotenv import load_dotenv
load_dotenv()
app = FastAPI()
#app.include_router(user)
app.include_router(news)