
from fastapi import HTTPException
from src.config import settings
import httpx
from src.spotify.utils import spotify_request


async def get_token_identity(access_token: str):
    me=await spotify_request(
        "GET", 
        "https://api.spotify.com/v1/me",
        headers={"Authorization": f"Bearer {access_token}"}
    )
    return me


async def get_token_data(code: str):
    token_data=await spotify_request(
        "POST",
        "https://accounts.spotify.com/api/token",
        data={
                "grant_type": "authorization_code",
                "code": code,
                "redirect_uri":"http://127.0.0.1:8000/api/auth/callback",
                "client_id": settings.SPOTIPY_CLIENT_ID,
                "client_secret": settings.SPOTIPY_CLIENT_SECRET,
            },
            # auth=(settings.SPOTIPY_CLIENT_ID, settings.SPOTIPY_CLIENT_SECRET),
        headers={"Content-Type": "application/x-www-form-urlencoded"})
    
    
    return token_data


async def access_from_refresh(user_token: str):
    resp=await spotify_request(
        "POST",
        "https://accounts.spotify.com/api/token",
        data={
            "grant_type": "refresh_token",
            "refresh_token": user_token,
        },
        auth=(settings.SPOTIPY_CLIENT_ID, settings.SPOTIPY_CLIENT_SECRET),
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    return resp