from fastapi import APIRouter, Depends, Request, Response
from typing import Annotated

from infrastructure.services.redis_service import RedisService
from api.dependencies import redis_service

from infrastructure.schemas.admin_schemas import SAdminLogin

from infrastructure.utils.auth import generate_session_id
from api.actions.auth import authenticate_admin


router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/login/")
async def login(
    response: Response,
    data: SAdminLogin,
    redis_service: Annotated[RedisService, Depends(redis_service)]
) -> None:
    admin = await authenticate_admin(data)

    session_id = generate_session_id()

    response.set_cookie(key="Authorization", value=session_id, httponly=True)
    await redis_service.set(name=session_id, value=str(admin.id))


@router.post("/logout/")
async def logout(
    response: Response,
    request: Request,
    redis_service: Annotated[RedisService, Depends(redis_service)]
) -> None:
    session_id = request.cookies.get("Authorization")
    
    response.delete_cookie(key="Authorization")
    await redis_service.delete(session_id)





     



