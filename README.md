# News API

### Creeating News app with fastapi and Mongodb using the newsapi.org 

For this project, we musst first install lokal mongodb, fastapi, requirement  and postman. The frontend is developed using React and Bootstrap to display the news articles in an interactive and user-friendly manner.

## Getting started

![](img/resultFront.jpeg)



## Stack management(backend)

1. Open a command prompt at the root of the application's folder and cd backend.

2. add a new .env file and then the codes in the env.simple in . env 
3. Install the backend dependencies: pip install -r requirements.txt
4. Run: `uvicorn app:index --reload`

## Stack management(frontend)

1. Open a command prompt at the root of the application's folder and cd frontend.

2. add a new .env file and then the codes in the env.simple in . env 
3. Install the frontend dependencies: cd frontend && npm install

3. Run: `npm run start`



## How can I get API-Key
1. go to the OpenWeatherMap website (`https://newsapi.org/`) and to get the current weather. OpenWeatherMap is free to use.

2. register on the website and then go to meu => `My API Keys`
3.  create a new file as .env and added here API-key