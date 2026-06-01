from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.recommendation_schema import RecommendationRequest
from app.services.recommendation_service import get_recommendations

router = APIRouter()

@router.post("/recommendations")
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