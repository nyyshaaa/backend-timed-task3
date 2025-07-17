from fastapi import Depends, FastAPI
from src.auth.routes import spotify_auth_router
from src.db.dependencies import get_session
from src.spotify.routes import spotify_router
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

app = FastAPI()

app.include_router(spotify_auth_router, prefix="/api/auth")
app.include_router(spotify_router, prefix="/api/spotify")

@app.get("/health")
async def health_check(db_session:AsyncSession=Depends(get_session)):
    try:
        stmt=text("SELECT 1")  
        await db_session.execute(stmt)
        return {"status": "healthy"}
    except Exception as e:
        return {"status": "unhealthy", "details": str(e)}

