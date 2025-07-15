
from fastapi import APIRouter, Depends, HTTPException

spotify_router= APIRouter()

from fastapi import APIRouter, Depends
from src.spotify.dependencies import spotify_token_dependency
from src.spotify.services import (
    get_top_tracks, get_now_playing, start_playback
)


@spotify_router.get("/top_tracks")
async def top_tracks(
    access_token: str = Depends(spotify_token_dependency)
):
    """Returns your top 10 tracks"""
    data = await get_top_tracks(access_token)
    items = data.get("items", [])


    return [
        {
            "name":    track["name"],
            "artists": [artist["name"] for artist in track["artists"]],
            "album":   track["album"]["name"],
            "uri":     track["uri"],
            "url":     track["external_urls"]["spotify"]
        }
        for track in items
    ]

@spotify_router.get("/now_playing")
async def now_playing(
    access_token: str = Depends(spotify_token_dependency)
):
    """Returns the currently playing track"""
    data = await get_now_playing(access_token)
    item=data.get("item",{}) 
    if not item:
        return {"status": "No track currently playing"}
    return {"name":item["name"],"artists":item["artists"],"uri":item["uri"]}


@spotify_router.put("/play/{track_id}")
async def play_track(
    track_id: str,
    access_token: str = Depends(spotify_token_dependency)
):
    """Starts playing a specific track from your top list"""
    top = await get_top_tracks(access_token, limit=10)
    valid_uris = {t["uri"] for t in top["items"]}

    uri = f"spotify:track:{track_id}"
    if uri not in valid_uris:
        raise HTTPException(
            status_code=400,
            detail=f"Track {track_id} is not in your Top 10."
        )
    
    await start_playback(access_token, uri)
    return {"status": "playing", "track_id": track_id}