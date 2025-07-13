
import httpx
from fastapi import HTTPException
from src.config import settings

async def get_access_token(code: str):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://accounts.spotify.com/api/token",
            data={
                "grant_type": "authorization_code",
                "code": code,
                "redirect_uri": settings.SPOTIPY_REDIRECT_URI,
                "client_id": settings.SPOTIPY_CLIENT_ID,
                "client_secret": settings.SPOTIPY_CLIENT_SECRET,
            },
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    return response.json()
