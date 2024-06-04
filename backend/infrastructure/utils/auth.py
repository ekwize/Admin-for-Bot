from passlib.context import CryptContext
from uuid import uuid4


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def generate_session_id() -> str:
    return str(uuid4())


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(password: str, hashed_password: str) -> bool:
    return pwd_context.verify(password, hashed_password)
