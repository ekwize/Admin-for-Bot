from fastapi import Request, status, HTTPException
from functools import wraps

from infrastructure.services.redis_service import RedisService
from infrastructure.services.admin_service import AdminService

from api.actions.auth import get_admin


def is_superadmin(func):
    @wraps(func)
    async def wrapper(
        request: Request,
        redis_service: RedisService,
        admin_service: AdminService,
        *args,
        **kwargs
    ):
        admin = await get_admin(request, redis_service, admin_service)

        if not admin.is_superadmin:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
        
        return await func(request, redis_service, admin_service, *args, **kwargs)

    return wrapper


def auth_required(func):
    @wraps(func)
    async def wrapper(
        request: Request,
        redis_service: RedisService,
        admin_service: AdminService,
        *args,
        **kwargs
    ):
        await get_admin(request, redis_service, admin_service)
        return await func(request, redis_service, admin_service, *args, **kwargs)

    return wrapper
