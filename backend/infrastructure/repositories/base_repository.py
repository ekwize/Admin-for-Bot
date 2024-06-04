from abc import ABC, abstractmethod
from typing import NoReturn


class AbstractRepository(ABC):

    @abstractmethod
    async def create(self, **kwargs) -> NoReturn:
        raise NotImplementedError

    @abstractmethod
    async def update(self, **kwargs) -> NoReturn:
        raise NotImplementedError

    @abstractmethod
    async def delete(self, **kwargs) -> NoReturn:
        raise NotImplementedError

    @abstractmethod
    async def get_single(self, **kwargs) -> NoReturn:
        raise NotImplementedError
    
    @abstractmethod
    async def get_all(self, **kwargs) -> NoReturn:
        raise NotImplementedError
    
    @abstractmethod
    async def count(self, **kwargs) -> NoReturn:
        raise NotImplementedError