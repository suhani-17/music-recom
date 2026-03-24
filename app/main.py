from fastapi import FastAPI
from app.routers import recommendation

app = FastAPI()

@app.get("/")

def root():
    return {"message": "Backend is running!"}

app.include_router(recommendation.router)