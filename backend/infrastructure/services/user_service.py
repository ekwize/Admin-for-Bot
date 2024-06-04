from infrastructure.repositories.database_repository import DatabaseRepository
from infrastructure.models.user import User
from infrastructure.schemas.user_schemas import SUserCreate, SUserUpdate


class UserService:
    
    def __init__ (self, repo: DatabaseRepository[User]):
        self._repo: DatabaseRepository[User] = repo(model=User)

    async def create(self, data: SUserCreate) -> SUserCreate:
        user_data = data.model_dump()
        user = await self._repo.create(user_data)

        return user

    async def update(self, data: SUserUpdate, **filters) -> SUserUpdate:
        user_data = data.model_dump()
        user = await self._repo.update(user_data, **filters)

        return user

    async def delete(self, **filters) -> None:
        await self._repo.delete(**filters)

    async def get_single(self, **filters):
        return await self._repo.get_single(**filters)
    
    async def get_all(self, **filters):
        return await self._repo.get_all(**filters)
    
    async def count(self, **filters):
        return await self._repo.count(**filters)