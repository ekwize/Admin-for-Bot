from fastapi import APIRouter

from admin.api.routes.admin_actions.auth import router as admin_auth_router
from admin.api.routes.admin_actions.info import router as admin_info_router 
from admin.api.routes.admin_actions.utils import router as admin_utils_router

from admin.api.routes.user_actions.utils import router as user_utils_router
from admin.api.routes.user_actions.info import router as user_info_router


v1 = APIRouter(prefix="/api")

v1.include_router(admin_auth_router)

v1.include_router(admin_info_router)
v1.include_router(user_info_router)

v1.include_router(admin_utils_router)
v1.include_router(user_utils_router)

