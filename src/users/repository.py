from sqlmodel import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.users.models import User

async def get_user_by_id(session: AsyncSession, spotify_id: str) -> User | None:
    result = await session.execute(
        select(User).where(User.spotify_id == spotify_id)
    )
    return result.scalar_one_or_none()

async def get_user_token_by_id(session: AsyncSession, spotify_id: str) -> str | None:
    result = await session.execute(
        select(User.refresh_token).where(User.spotify_id == spotify_id)
    )
    return result.scalar_one_or_none()

async def create_or_update_user(
    session: AsyncSession,
    spotify_id: str,
    email: str | None,
    refresh_token: str
) -> User:
    user = await get_user_by_id(session, spotify_id)
    if user:
        user.refresh_token = refresh_token

    else:
        user = User(
            spotify_id=spotify_id,
            email=email,
            refresh_token=refresh_token
        )
        session.add(user)
    await session.commit()
    return user