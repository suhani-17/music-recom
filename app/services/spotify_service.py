import time
import httpx
import os
import base64
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

access_token = None
token_expiry = 0

async def get_spotify_token(force_refresh: bool = False):
    global access_token , token_expiry

    #if token exists and is not expired, reuse
    if not force_refresh and access_token and time.time() < token_expiry:
        return access_token
    
    #else fetch new token 
    auth_str = f"{client_id}:{client_secret}"
    b64_auth = base64.b64encode(auth_str.encode()).decode()

    headers = {
        "Authorization": f"Basic {b64_auth}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "client_credentials"
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://accounts.spotify.com/api/token",
            headers=headers,
            data=data
        )

    token_data = response.json()

    access_token = token_data.get("access_token")
    expires_in = token_data.get("expires_in", 3600) # default to

    #set expiry buffer 
    token_expiry = time.time() + expires_in - 60 # buffer of 60 seconds

    return access_token