from infrastructure.repositories.database_repository import DatabaseRepository

from infrastructure.services.user_service import UserService
from infrastructure.models.user import User


def user_service():
    return UserService(DatabaseRepository[User])