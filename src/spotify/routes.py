
from fastapi import APIRouter, Depends, HTTPException, Path

spotify_router= APIRouter()

from fastapi import APIRouter, Depends
from src.auth.dependencies import spotify_token_dependency
from src.spotify.services import (
    get_top_tracks, get_now_playing, pause_playback, start_playback
)


@spotify_router.get("/top_tracks")
async def top_tracks(
    limit: int = 10,
    access_token: str = Depends(spotify_token_dependency)
):
    """Returns your top tracks"""
    data = await get_top_tracks(access_token, limit=limit)
    items = data.get("items", [])

    if not items:
        return {"status": "No top tracks found"}
    
    return [
        {
            "name":    track["name"],
            "artists": [artist["name"] for artist in track["artists"]],
            "album":   track["album"]["name"],
            "uri":     track["uri"],
            "url":     track["external_urls"]["spotify"],
            "id":     track["id"]
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
   
    return {"name":item["name"],"artists":item["artists"],"uri":item["uri"],"id":item["id"],"url":item["external_urls"]["spotify"]}


@spotify_router.put("/top_tracks/play/{position}")
async def play_track(
    position: int=Path(
        ...,
        ge=0,
        le=9,
        description="Position of the track in your top 10"
    ),
    access_token: str = Depends(spotify_token_dependency)
):
    """Starts playing a specific track from your top list"""
    #Get 1 track/song out of top-10 by offset(position)
    track_by_pos = await get_top_tracks(access_token, limit=1,offset=position)
    items = track_by_pos.get("items", []) # response will be list of 1 item
    if not items:
        raise HTTPException(404, f"No track found at position {position}")

    track = items[0]
    track_id = track["id"]

    print(track_id)
    print(track["name"])

    uri = f"spotify:track:{track_id}"

    
    await start_playback(access_token, uri)
    
    return {
        "status": "playing",
        "position": position,
        "track_uri": uri,
        "name": track["name"],
        "artists": track["artists"],
    }

@spotify_router.put("/pause")
async def pause(
    access_token: str = Depends(spotify_token_dependency)
):
    """Pauses the currently playing track"""
    await pause_playback(access_token)
    return {"status": "paused"}