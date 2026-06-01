from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.recommendation_schema import RecommendationRequest, RecommendationResponse
from app.services.recommendation_service import get_recommendations
from app.models.history import History

router = APIRouter()

@router.post("/recommendations", response_model=RecommendationResponse)
async def recommend(data: RecommendationRequest, db: Session = Depends(get_db)):
    result = await get_recommendations(data.mood, data.language)

    for song in result:
        record = History(
            mood = data.mood,
            language = data.language,
            song_id = song['id'],
            title = song['title'],
            artist = song['artist'],
        )
        db.add(record)

        db.commit()
    return {
        "success": True,
        "status_code": 200,
        "data": result
    }