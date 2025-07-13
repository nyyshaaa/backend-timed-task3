from fastapi import FastAPI
from src.spotify.auth import spotify_auth_router
from src.spotify.routes import spotify_router

app = FastAPI()

app.include_router(spotify_auth_router, prefix="/auth/spotify")
app.include_router(spotify_router, prefix="/spotify")   

@app.get("/")
def read_root():
    return {"message": "Welcome to the Spotify API wrapper"}
