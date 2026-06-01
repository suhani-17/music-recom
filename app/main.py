from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  
from app.routers import recommendation

from app.db.database import engine 
from app.models.history import History


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Adjust this in production to restrict origins
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)   

@app.get("/")
def root():
    return {"message": "Backend is running!"}

#temporary code to create tables on startup, in production use alembic for migrations
@app.on_event("startup")
def create_tables():
    History.metadata.create_all(bind=engine)

app.include_router(recommendation.router)