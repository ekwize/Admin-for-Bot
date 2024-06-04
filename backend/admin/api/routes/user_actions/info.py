from fastapi import APIRouter, Depends, Request
from typing import Annotated

from infrastructure.services.user_service import UserService
from api.dependencies import user_service

from infrastructure.services.redis_service import RedisService
from api.dependencies import redis_service

from infrastructure.services.admin_service import AdminService
from api.dependencies import admin_service

from infrastructure.schemas.user_schemas import SGetUserByUsername,  SUserView

from api.actions.permissions import auth_required


router = APIRouter(prefix="/info", tags=["User Info"])


@router.post("/user/", response_model=SUserView | None)
@auth_required
async def get_user(
    request: Request,
    redis_service: Annotated[RedisService, Depends(redis_service)],
    admin_service: Annotated[AdminService, Depends(admin_service)],
    user_service: Annotated[UserService, Depends(user_service)],
    user_info: SGetUserByUsername
) -> SUserView | None:
    user = await user_service.get_single(username=user_info.username)
    return user


@router.get("/user/all/", response_model=list[SUserView])
@auth_required
async def get_all_users(
    request: Request,
    redis_service: Annotated[RedisService, Depends(redis_service)],
    admin_service: Annotated[AdminService, Depends(admin_service)],
    user_service: Annotated[UserService, Depends(user_service)]
) -> list[SUserView]:
    users = await user_service.get_all()
    return users


@router.get("/user/count/")
@auth_required
async def get_users_count(
    request: Request,
    redis_service: Annotated[RedisService, Depends(redis_service)],
    admin_service: Annotated[AdminService, Depends(admin_service)],
    user_service: Annotated[UserService, Depends(user_service)]
) -> int:
    user_count = await user_service.count()
    return user_count

    

