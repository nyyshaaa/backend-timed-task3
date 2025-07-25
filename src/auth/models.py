# src/users/identities.py
from sqlmodel import SQLModel, Field, Column
from datetime import datetime

class UserIdentity(SQLModel, table=True):
    __tablename__ = "creds"

    id: int = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id", nullable=False, index=True)
    provider: str = Field(nullable=False)         # e.g. 'spotify'
    provider_user_id: int = Field(nullable=False,unique=True)  # e.g. Spotify’s own user ID
    refresh_token: str | None = None
    access_token: str | None = None
    token_expires_at: datetime | None = None
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
