import os
from typing import AsyncGenerator
from dotenv import find_dotenv, load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from db.models import Base

load_dotenv(find_dotenv())

engine = create_async_engine(os.getenv('DB_URI'), echo=True)
sessionmaker = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

async def create_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def drop_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with sessionmaker() as session:
        yield session