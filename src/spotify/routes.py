
from fastapi import APIRouter, Depends, HTTPException, Query, Request
from fastapi.responses import RedirectResponse
from src.config import settings
from src.spotify.auth import get_access_token, refresh_access_token

router = APIRouter()

@router.get("/login")
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

@router.get("/callback")
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

@router.get("/refresh_token")
async def refresh_token(refresh_token: str):
    return await refresh_access_token(refresh_token)
