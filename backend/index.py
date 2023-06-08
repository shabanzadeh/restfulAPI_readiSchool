
from fastapi import FastAPI
#from routes.user import user
from dotenv import load_dotenv
load_dotenv()
from fastapi.middleware.cors import CORSMiddleware
from routes.news import news
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4000"],  # Add the allowed origin(s) here
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)
#app.include_router(user)
app.include_router(news)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)