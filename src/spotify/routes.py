
from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import RedirectResponse
from src.config import settings
from src.spotify.auth import get_access_token

router = APIRouter()

@router.get("/login")
async def login():
    auth_url = (
        f"https://accounts.spotify.com/authorize?"
        f"client_id={settings.SPOTIPY_CLIENT_ID}&"
        f"response_type=code&"
        f"redirect_uri={settings.SPOTIPY_REDIRECT_URI}&"
        f"scope={settings.SPOTIPY_SCOPE}"
    )
    print(f"DEBUG: Spotify Authorization URL: {auth_url}")
    return RedirectResponse(auth_url)

@router.get("/callback")
async def callback(code: str):
    return await get_access_token(code)
