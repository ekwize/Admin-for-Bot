from uuid import UUID
from pydantic import EmailStr
from infrastructure.schemas.base_schema import Base


class SAdmin(Base):
    """ 
    Schema for create and update admin
    """

    first_name: str
    last_name: str
    email: EmailStr
    phone_number: str
    login: str
    password: str
    is_superadmin: bool


class SAdminUpdate(SAdmin):
    ...


class SAdminView(Base):
    """
    Schema for view admin
    """
    id: UUID
    first_name: str
    last_name: str
    email: str
    phone_number: str
    login: str
    is_superadmin: bool


class SAdminLogin(Base):
    """
    Schema for login admin
    """
    
    login: str
    password: str

class SGetAdminByLogin(Base):
    """
    Schema for get admin by login
    """

    login: str



class SessionId(Base):
    session_id: str