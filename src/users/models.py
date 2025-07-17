from sqlmodel import SQLModel, Field

class User(SQLModel, table=True):
    __tablename__ = "users"

    spotify_id: str = Field(primary_key=True, index=True)
    email:      str | None = Field(default=None, unique=True)
    refresh_token: str