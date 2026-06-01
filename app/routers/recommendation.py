from fastapi import APIRouter
from app.schemas.recommendation_schema import RecommendationRequest
from app.services.recommendation_service import get_recommendations

router = APIRouter()

@router.post("/recommendations")
async def recommend(data: RecommendationRequest):
    result = await get_recommendations(data.mood, data.language)
    return {
        "success": True,
        "status_code": 200,
        "data": result
    }