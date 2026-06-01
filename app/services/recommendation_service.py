import httpx
import os
from dotenv import load_dotenv
from app.services.spotify_service import get_spotify_token

load_dotenv()

SPOTIFY_URL = "https://api.spotify.com/v1/search"

async def fetch_spotify_data(query: str, token: str):
   headers = {
        "Authorization": f"Bearer {token}"
   }

   params = {
         "q": query,
         "type": "track",
         "limit": 10,
         "market": "IN"
   }
   async with httpx.AsyncClient() as client:
        response = await client.get(SPOTIFY_URL, headers=headers, params=params)
        return response


async def get_recommendations ( mood: str, language: str) : 

   query = f"{mood} {language}"

   token = await get_spotify_token()

   response = await fetch_spotify_data(query, token)

   #handle expired token case
   if response.status_code == 401:
      token = await get_spotify_token(force_refresh=True) 
      response = await fetch_spotify_data(query, token) 

      if response.status_code == 401:
            raise Exception("Spotify authentication failed")

   #other errors 
   if response.status_code != 200:
      raise Exception(f"Spotify API error: {response.status_code} - {response.text}")

   try: 
       data = response.json()
   except Exception as e:
         raise Exception(f"Invalid Response!: {str(e)}")  

   tracks = data.get("tracks", {}).get("items", [])
   return transform_tracks(tracks)
       

       
   
def transform_tracks(tracks):
     result = [] 

     for track in tracks:
         
         # Extract relevant information from each track
         track_id = track.get("id")
         title = track.get("name")

         # Extract artist 
         artists = track.get("artists") or []
         artist_name = artists[0].get("name") if artists else "Unknown Artist"
         

         # Extract image
         album = track.get("album") or {}
         images =  album.get("images") or []
         image_url = images[0]["url"] if images else None

         # Extract preview URL
         preview_url = track.get("preview_url")

         if not track_id or not title:
             continue
         
         result.append({
             "id": track_id,
             "title": title,
             "artist": artist_name,
             "image_url": image_url,
             "preview_url": preview_url
         })
   
     return result
