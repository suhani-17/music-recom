from fastapi import APIRouter
from app.schemas.recommendation_schema import RecommendationRequest

router = APIRouter()

@router.post("/recommendations")
async def recommend(data: RecommendationRequest):
    return{
        "message" : "API is working",
        "input" : data
    }