
from urllib.parse import urlencode
from fastapi.params import Cookie
from fastapi.responses import JSONResponse, RedirectResponse
import httpx
from fastapi import APIRouter, Depends, HTTPException, Query
from src.auth.services import access_from_refresh, get_token_identity, get_token_data
from src.config import settings
from src.db.dependencies import get_session
from src.users.repository import create_or_update_user, get_user_token_by_id
from src.spotify.utils import spotify_request

spotify_auth_router = APIRouter()

@spotify_auth_router.get("/login")
async def login():
    params = {
        "client_id":     settings.SPOTIPY_CLIENT_ID,
        "response_type": "code",
        "redirect_uri":  "http://127.0.0.1:8000/api/auth/callback",
        "scope":         settings.SPOTIPY_SCOPE,
    }
    auth_url = "https://accounts.spotify.com/authorize?" + urlencode(params)
    return RedirectResponse(auth_url)

@spotify_auth_router.get("/callback")
async def callback(code: str = Query(...),session = Depends(get_session)):
    """
    Spotify will redirect here with ?code=<authorization_code>.
    We exchange that code for access_token + refresh_token.
      1) Exchange code → access_token + refresh_token
      2) Fetch /v1/me to get the Spotify user’s stable ID
      3) Store refresh_token in our DB under that Spotify ID and keep it server side only and don't return it to client.
      4) Return a response with the access_token and set a cookie with the spotify_id.
    """
    # get_token_data should POST to /api/token with grant_type=authorization_code
    token_data = await get_token_data(code=code)

    access_token=token_data["access_token"]
    refresh_token= token_data["refresh_token"]
    expires_in = token_data.get("expires_in")

    # 2) Fetch user profile 
    profile= await get_token_identity(access_token)
    spotify_id = profile["id"]
    spotify_email = profile.get("email")

    # 3) Store refresh_token
    await create_or_update_user(
        session, spotify_id, spotify_email, refresh_token
    )

    response= JSONResponse(content={"message": "Spotify connected", "spotify_id": spotify_id,"access_token": access_token})
    response.set_cookie(
        key="spotify_id",
        value=spotify_id,
        httponly=True,       # inaccessible to JS
        secure=True,         # only over HTTPS in production
        samesite="lax",      # prevent CSRF in most cases
        max_age=60*60*6*1  # e.g. 6 hours
    )
    return response
 

@spotify_auth_router.get("/refresh")
async def refresh_token(
    spotify_id: str = Cookie(..., description="Set by /api/auth/callback"),
    session = Depends(get_session)):
    """
    Endpoint to refresh the Spotify access token using the stored refresh_token.
    """
    user_token = await get_user_token_by_id(session, spotify_id)
    if not user_token:
        raise HTTPException(status_code=401, detail="Spotify user not registered.")

    data = await access_from_refresh(user_token)
    
    return {"access_token": data["access_token"], "expires_in": data.get("expires_in")}
    


