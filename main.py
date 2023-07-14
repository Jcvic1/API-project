import models, note, authentication, date_time
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine



models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/api/v1/healthchecker")
def root():
    return {"message": "Welcome to FastAPI with SQLAlchemy"}


app.include_router(authentication.router, tags=['Users'], prefix='/api/v1')
app.include_router(note.router, tags=['Notes(OAuth2, password)'], prefix='/api/v1')
app.include_router(date_time.router, tags=['Date-Time(apiKey)'], prefix='/api/v1')




