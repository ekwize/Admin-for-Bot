from fastapi import HTTPException, Request, status

from infrastructure.services.redis_service import RedisService
from infrastructure.services.admin_service import AdminService

from infrastructure.models.admin import Admin
from infrastructure.schemas.admin_schemas import SAdminLogin

from infrastructure.utils.auth import verify_password
from api.dependencies import admin_service 


async def authenticate_admin(data: SAdminLogin) -> Admin:
    admin = await admin_service().get_single(login=data.login)

    if not (admin and verify_password(data.password, admin.password)):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect password or username"
        )
    return admin


async def get_admin(
    request: Request,
    redis_service: RedisService,
    admin_service: AdminService,
) -> Admin:
    session_id = request.cookies.get("Authorization")

    if not session_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    
    admin_id = await redis_service.get(session_id)
    admin = await admin_service.get_single(id=admin_id)

    if not admin:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    
    return admin
    