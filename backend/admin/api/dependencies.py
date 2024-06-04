from fastapi import Depends

from infrastructure.services.bot_service import BotService
from aiogram import Bot

from infrastructure.services.redis_service import RedisService
from infrastructure.core.redis import init_redis_pool
from redis.asyncio import Redis

from infrastructure.repositories.database_repository import DatabaseRepository

from infrastructure.services.user_service import UserService
from infrastructure.models.user import User

from infrastructure.services.admin_service import AdminService
from infrastructure.models.admin import Admin

from settings import settings


def admin_service():
    return AdminService(DatabaseRepository[Admin])


def user_service():
    return UserService(DatabaseRepository[User])


def redis_service(redis: Redis = Depends(init_redis_pool)):
    return RedisService(redis)


def bot_service():
    return BotService(Bot(settings.BOT_TOKEN))

