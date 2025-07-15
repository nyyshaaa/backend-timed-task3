
from fastapi.responses import RedirectResponse
import httpx
from fastapi import APIRouter, HTTPException, Query
from src.config import settings

spotify_auth_router = APIRouter()

async def get_access_token(code: str):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://accounts.spotify.com/api/token",
            data={
                "grant_type": "authorization_code",
                "code": code,
                "redirect_uri": "http://127.0.0.1:8000/auth/spotify/callback",
                "client_id": settings.SPOTIPY_CLIENT_ID,
                "client_secret": settings.SPOTIPY_CLIENT_SECRET,
            },
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    return response.json()




@spotify_auth_router.get("/login")
async def login():
    print(f"DEBUG: SPOTIPY_REDIRECT_URI from settings: {settings.SPOTIPY_REDIRECT_URI}")
    auth_url = (
        f"https://accounts.spotify.com/authorize?"
        f"client_id={settings.SPOTIPY_CLIENT_ID}&"
        f"response_type=code&"
        f"redirect_uri=http://127.0.0.1:8000/auth/spotify/callback&"
        f"scope={settings.SPOTIPY_SCOPE}"
    )
    print(f"DEBUG: Spotify Authorization URL: {auth_url}")
    return RedirectResponse(auth_url)

@spotify_auth_router.get("/callback")
async def callback(code: str = Query(...)):
    """
    Spotify will redirect here with ?code=<authorization_code>.
    We exchange that code for access_token + refresh_token.
    """
    try:
        # get_access_token should POST to /api/token with grant_type=authorization_code
        token_data = await get_access_token(
            code=code
        )
    except HTTPException as e:
        # bubble up any HTTP errors from Spotify
        raise e

    # token_data must include: access_token, refresh_token, expires_in, scope, token_type
    return {
        "access_token": token_data["access_token"],
        "refresh_token": token_data["refresh_token"],
        "expires_in": token_data.get("expires_in"),
        "scope": token_data.get("scope"),
        "token_type": token_data.get("token_type"),
    }





