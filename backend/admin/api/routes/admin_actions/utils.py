from fastapi import APIRouter, Depends, Request
from typing import Annotated

from infrastructure.services.redis_service import RedisService
from api.dependencies import redis_service

from infrastructure.services.admin_service import AdminService
from api.dependencies import admin_service

from infrastructure.schemas.admin_schemas import SAdmin

from api.actions.permissions import is_superadmin


router = APIRouter(prefix="/utils", tags=["Admin Utils"])


@router.post("/createadmin/")
@is_superadmin
async def create_admin(
    request: Request,
    redis_service: Annotated[RedisService, Depends(redis_service)],
    admin_service: Annotated[AdminService, Depends(admin_service)],
    admin: SAdmin,
) -> None:
    await admin_service.create(admin)


