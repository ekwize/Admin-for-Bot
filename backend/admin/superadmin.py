from sqlalchemy import select
from settings import settings

from infrastructure.models.admin import Admin
from infrastructure.core.database import async_session
from infrastructure.utils.auth import hash_password


async def superadmin_auto_create() -> Admin:

    async with async_session() as session:
        query = select(Admin).filter_by(id=settings.SUPERADMIN_ID)
        superadmin_exists = await session.scalar(query)

        if superadmin_exists:
            return "Super-admin already exists"

        superadmin = Admin(
            id=settings.SUPERADMIN_ID,
            first_name=settings.SUPERADMIN_FIRST_NAME,
            last_name=settings.SUPERADMIN_LAST_NAME,
            email=settings.SUPERADMIN_EMAIL,
            phone_number=settings.SUPERADMIN_PHONE,
            login=settings.SUPERADMIN_LOGIN,
            password=hash_password(settings.SUPERADMIN_PASSWORD),
            is_superadmin=True
        )
        session.add(superadmin)
        await session.commit()
        await session.refresh(superadmin)

        return superadmin
    
   