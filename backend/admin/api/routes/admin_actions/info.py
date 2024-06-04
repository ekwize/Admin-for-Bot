from fastapi import APIRouter, Depends, Request
from typing import Annotated

from infrastructure.services.redis_service import RedisService
from api.dependencies import redis_service

from infrastructure.services.admin_service import AdminService
from api.dependencies import admin_service

from infrastructure.schemas.admin_schemas import SAdminView, SGetAdminByLogin

from api.actions.permissions import auth_required


router = APIRouter(prefix="/info", tags=["Admin Info"])


@router.post("/admin/", response_model=SAdminView)
@auth_required
async def get_admin(
    request: Request,
    redis_service: Annotated[RedisService, Depends(redis_service)],
    admin_service: Annotated[AdminService, Depends(admin_service)],
    admin_info: SGetAdminByLogin
) -> SAdminView:
    admin = await admin_service.get_single(login=admin_info.login)
    return admin


@router.get("/admin/all/", response_model=list[SAdminView])
@auth_required
async def get_all_admins(
    request: Request,
    redis_service: Annotated[RedisService, Depends(redis_service)],
    admin_service: Annotated[AdminService, Depends(admin_service)]
) -> list[SAdminView]:
    admins = await admin_service.get_all()
    return admins

@router.get("/admin/count/")
@auth_required
async def get_admin_count(
    request: Request,
    redis_service: Annotated[RedisService, Depends(redis_service)],
    admin_service: Annotated[AdminService, Depends(admin_service)]
) -> int:
    count = await admin_service.count()
    return count



    

