import http
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
import httpx
from fastapi import Depends, HTTPException, Header
from sqlalchemy.ext.asyncio import  AsyncSession
from src.auth.services import get_token_identity
from src.config import settings
from src.db.dependencies import get_session
from src.users.repository import get_user_by_id, get_user_token_by_id

auth_bearer = HTTPBearer()

# Social login only Authentication
async def spotify_access_token(
    creds: HTTPAuthorizationCredentials = Depends(auth_bearer),
    session: AsyncSession = Depends(get_session)
):
    
    access_token = creds.credentials
    
    # like decoding the JWT , but here we check the access token with Spotify API
    profile = await get_token_identity(access_token)

    spotify_id = profile["id"]
    
    # Lookup user in db by spotify_id
    user = await get_user_by_id(session, spotify_id)
    if not user:
        raise HTTPException(401, "Spotify user not registered.")

    return access_token


# experimental -----------------------------------
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