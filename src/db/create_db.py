# create_db.py
from sqlmodel import SQLModel
from src.users.models import User
from sqlmodel import create_engine
from src.config import settings


engine = create_engine(
    settings.SYNC_DATABASE_URL,
    echo=True
)

def init_db() -> None:
    """
    Creates all tables defined by your SQLModel models.
    Run this *once* (or whenever your schema changes - only for normal add columns ,tables migrations).
    Move to alembic for heavy migrations.
    """
    SQLModel.metadata.create_all(engine)
    print("✅ Tables created or already exist.")

if __name__ == "__main__":
    init_db()

# Important tips:
# Run via -- python -m src.db.create_db
# Restart vscode if new libarary is installed to ensure it is recognized for retrieving env variables which may use that library.
