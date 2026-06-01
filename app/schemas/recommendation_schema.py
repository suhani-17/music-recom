from pydantic import BaseModel
from enum import Enum

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