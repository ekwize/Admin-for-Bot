from redis.asyncio import Redis
from redis.asyncio.client import KeyT

class RedisService:

    def __init__(self, redis: Redis):
        self._redis: Redis = redis

    async def get(self, name: KeyT):
        return await self._redis.get(name)

    async def set(self, **kwargs):
        await self._redis.set(**kwargs)

    async def delete(self, *names: KeyT):
        await self._redis.delete(*names)

    