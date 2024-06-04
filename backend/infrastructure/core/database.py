from typing import AsyncGenerator
from settings import settings

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine


DB_URL = settings.build_postgres_dsn()


engine = create_async_engine(DB_URL)                           
async_session = async_sessionmaker(engine, expire_on_commit=False)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session