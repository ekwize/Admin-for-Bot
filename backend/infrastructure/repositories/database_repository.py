from sqlalchemy import func, select, update, delete

from infrastructure.core.database import async_session
from infrastructure.repositories.base_repository import AbstractRepository
from infrastructure.models.base import Base as BaseModel
from infrastructure.schemas.base_schema import Base as BaseSchema


class DatabaseRepository[ModelType: BaseModel](AbstractRepository):

    def __init__(self, model: type[ModelType]):
        self._model: type[ModelType] = model

    async def create(self, data: BaseSchema) -> ModelType:
        async with async_session() as session:
            instance = self._model(**data)

            session.add(instance)
            await session.commit()
            await session.refresh(instance)
            return instance
        
    async def update(self, data: BaseSchema, **filters) -> ModelType:
        async with async_session() as session:

            query = (
                update(self._model)
                .values(**data.model_dump())
                .filter_by(**filters)
                .returning(self._model)
            )
            res = await session.execute(query)
            await session.commit()
            return res.scalar_one()
        
    async def delete(self, **filters) -> None:
        async with async_session() as session:
            await session.execute(delete(self._model).filter_by(**filters))
            await session.commit()

    async def get_single(self, **filters) -> ModelType | None:
        async with async_session() as session:
            row = await session.execute(select(self._model).filter_by(**filters))
            return row.scalar_one_or_none()
        
    async def get_all(self, **filters) -> list[ModelType] | None:
        async with async_session() as session:
            rows = await session.execute(select(self._model).filter_by(**filters))
            return rows.scalars().all()
        
    async def count(self, **filters) -> int:
        async with async_session() as session:
            count = await session.execute(select(func.count()).select_from(self._model).filter_by(**filters))
            return count.scalar()
        
        

    
