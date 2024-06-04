from uuid import UUID, uuid4

from sqlalchemy.orm import Mapped, mapped_column
from infrastructure.models.base import Base


class Admin(Base):
    __tablename__ = "admins"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    # telegram_id: Mapped[int] = mapped_column(unique=True, ullable=False)
    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(unique=True)
    phone_number: Mapped[str] = mapped_column(unique=True)
    login: Mapped[str] = mapped_column(nullable=False, unique=True)
    password: Mapped[str] = mapped_column(nullable=False)
    is_superadmin: Mapped[bool] = mapped_column(nullable=False, default=False)