import httpx
from fastapi import HTTPException
from src.config import settings

async def spotify_token_dependency() -> str:
#    access_token = settings.ACCESS_TOKEN
#    return access_token

    refresh_token = settings.REFRESH_TOKEN
    async with httpx.AsyncClient() as client:
        resp = await client.post(
            "https://accounts.spotify.com/api/token",
            data={
                "grant_type": "refresh_token",
                "refresh_token": refresh_token,
                "client_id": settings.SPOTIPY_CLIENT_ID,
                "client_secret": settings.SPOTIPY_CLIENT_SECRET,
            },
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )
    if resp.status_code != 200:
        raise HTTPException(status_code=resp.status_code, detail=resp.json())

    data = resp.json()
    return data["access_token"]
 
