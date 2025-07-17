
from sqlalchemy.ext.asyncio import create_async_engine,async_sessionmaker,AsyncSession
from src.config import settings

async_engine=create_async_engine(settings.DATABASE_URL,echo=True)

async_session=async_sessionmaker(bind=async_engine,class_=AsyncSession,expire_on_commit=False)