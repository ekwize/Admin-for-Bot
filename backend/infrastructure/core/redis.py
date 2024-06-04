from typing import AsyncIterator
from settings import settings

from redis.asyncio import Redis, from_url


async def init_redis_pool() -> AsyncIterator[Redis]:
    session = from_url(settings.build_redis_dsn(), encoding="utf-8", decode_responses=True)
    yield session
    await session.close()