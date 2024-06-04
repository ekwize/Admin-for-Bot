from sqlalchemy.orm import Mapped, mapped_column
from infrastructure.models.base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True) 
    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=True)
    full_name: Mapped[str] = mapped_column(nullable=True)
    username: Mapped[str] = mapped_column(nullable=False)
    is_premium: Mapped[bool] = mapped_column(nullable=True)
    language_code: Mapped[str] = mapped_column(nullable=False)