from fastapi import FastAPI
from src.spotify.routes import router as spotify_router

app = FastAPI()

app.include_router(spotify_router, prefix="/spotify")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Spotify API wrapper"}
