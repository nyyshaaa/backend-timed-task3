import httpx
from fastapi import HTTPException

BASE = "https://api.spotify.com/v1"

async def get_top_tracks(access_token: str, limit: int = 10, offset: int = 0) -> dict:
    url = f"{BASE}/me/top/tracks?limit={limit}&offset={offset}"
    headers = {"Authorization": f"Bearer {access_token}"}
    async with httpx.AsyncClient() as client:
        resp = await client.get(url, headers=headers)
    if resp.status_code != 200:
        raise HTTPException(status_code=resp.status_code, detail=resp.json())
    return resp.json()

async def get_now_playing(access_token: str) -> dict:
    url = f"{BASE}/me/player/currently-playing"
    headers = {"Authorization": f"Bearer {access_token}"}
    async with httpx.AsyncClient() as client:
        resp = await client.get(url, headers=headers)
    if resp.status_code not in (200, 204):
        raise HTTPException(status_code=resp.status_code, detail=resp.json())
    return resp.json() if resp.status_code == 200 else {}


async def start_playback(access_token: str, track_uri: str) -> None:
    url = f"{BASE}/me/player/play"
    headers = {"Authorization": f"Bearer {access_token}"}
    body = {"uris": [track_uri]}
    async with httpx.AsyncClient() as client:
        resp = await client.put(url, json=body, headers=headers)
    if resp.status_code not in (204, 202):
        raise HTTPException(status_code=resp.status_code, detail=resp.json())