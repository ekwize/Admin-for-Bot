from infrastructure.repositories.database_repository import DatabaseRepository

from infrastructure.models.admin import Admin
from infrastructure.schemas.admin_schemas import SAdmin, SAdminUpdate

from infrastructure.utils.auth import hash_password

class AdminService:
    
    def __init__ (self, repo: DatabaseRepository[Admin]):
        self._repo: DatabaseRepository[Admin] = repo(model=Admin)

    async def create(self, data: SAdmin) -> SAdmin:
        if data.password:
            data.password = hash_password(data.password)

        admin_data = data.model_dump()
        admin = await self._repo.create(admin_data)

        return admin

    async def update(self, data: SAdminUpdate, **filters) -> SAdminUpdate:
        if data.password:
            data.password = hash_password(data.password)
            
        admin_data = data.model_dump()
        admin = await self._repo.update(admin_data, **filters)

        return admin

    async def delete(self, **filters) -> None:
        await self._repo.delete(**filters)

    async def get_single(self, **filters):
        return await self._repo.get_single(**filters)
    
    async def get_all(self, **filters):
        return await self._repo.get_all(**filters)
    
    async def count(self, **filters):
        return await self._repo.count(**filters)