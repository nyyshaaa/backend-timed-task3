
from src.spotify.utils import spotify_request

BASE = "https://api.spotify.com/v1"

async def get_top_tracks(access_token: str, limit: int = 10, offset: int = 0) -> dict:
    url = f"{BASE}/me/top/tracks?limit={limit}&offset={offset}"
    headers = {"Authorization": f"Bearer {access_token}"}
    resp=await spotify_request("GET", url, headers=headers)
    return resp

async def get_now_playing(access_token: str) -> dict:
    url = f"{BASE}/me/player/currently-playing"
    headers = {"Authorization": f"Bearer {access_token}"}
    resp=await spotify_request("GET", url, headers=headers)
    return resp


async def start_playback(access_token: str, track_uri: str) -> None:
    url = f"{BASE}/me/player/play"
    headers = {"Authorization": f"Bearer {access_token}"}
    body = {"uris": [track_uri]}
    await spotify_request("PUT", url, json=body, headers=headers)

async def pause_playback(access_token: str) -> None:
    url = f"{BASE}/me/player/pause"
    headers = {"Authorization": f"Bearer {access_token}"}
    await spotify_request("PUT", url, headers=headers)