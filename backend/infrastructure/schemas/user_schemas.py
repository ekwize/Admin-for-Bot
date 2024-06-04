from typing import Optional
from infrastructure.schemas.base_schema import Base


class SUserCreate(Base):
    id: int
    first_name: str
    last_name: Optional[str]
    full_name: Optional[str]
    username: str
    is_premium: Optional[bool]
    language_code: str


class SUserView(SUserCreate):
    ...


class SUserUpdate(Base):
    first_name: str
    last_name: Optional[str]
    full_name: Optional[str]
    username: str
    is_premium: bool
    language_code: int


class SGetUserByUsername(Base):
    username: str

class SUserCount(Base):
    user_count: int



