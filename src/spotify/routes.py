
from fastapi import APIRouter, Depends, HTTPException

spotify_router= APIRouter()

from fastapi import APIRouter, Depends
from src.spotify.dependencies import spotify_token_dependency
from src.spotify.services import (
    get_top_tracks, get_now_playing, pause_playback, start_playback
)


@spotify_router.get("/top_tracks")
async def top_tracks(
    access_token: str = Depends(spotify_token_dependency)
):
    """Returns your top 10 tracks"""
    data = await get_top_tracks(access_token)
    return {"top_tracks": data.get("items", [])}

@spotify_router.get("/now_playing")
async def now_playing(
    access_token: str = Depends(spotify_token_dependency)
):
    """Returns the currently playing track"""
    data = await get_now_playing(access_token)
    return {"now_playing": data}


@spotify_router.post("/play/{track_id}")
async def play_track(
    track_id: str,
    access_token: str = Depends(spotify_token_dependency)
):
    """Starts playing a specific track from your top list"""
    uri = f"spotify:track:{track_id}"
    await start_playback(access_token, uri)
    return {"status": "playing", "track_id": track_id}