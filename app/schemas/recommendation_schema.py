from pydantic import BaseModel
from enum import Enum
from typing import List, Optional

#we are excepting string to return string in response to that it works cleanly with json 

class Mood(str, Enum): 
    happy = "happy"
    sad = "sad"
    calm = "calm"
    energetic = "energetic"

class Language(str, Enum):
    english = "english"
    spanish = "spanish"



class RecommendationRequest(BaseModel):
    mood : Mood
    language: Language


class TrackResponse(BaseModel):
    id: str
    title: str
    artist: str
    image_url: Optional[str] = None
    preview_url: Optional[str] = None

class RecommendationResponse(BaseModel):
    success: bool
    status_code: int
    data: List[TrackResponse]