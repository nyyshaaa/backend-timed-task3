
# src/users/models.py
from sqlmodel import SQLModel, Field
from uuid import uuid4
from datetime import datetime

# class User(SQLModel, table=True):
#     __tablename__ = "users"

#     spotify_id: str = Field(primary_key=True, index=True)
#     email:      str | None = Field(default=None, unique=True)
#     refresh_token: str



class User(SQLModel, table=True):
    __tablename__ = "users"

    id: int = Field(default=None, primary_key=True)
    email: str | None = Field(default=None, unique=True)
    name: str | None = None
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)



