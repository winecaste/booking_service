from typing import TYPE_CHECKING

from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.database import Base

if TYPE_CHECKING:
    from app.bookings.models import Bookings


class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(nullable=False)
    hashed_password: Mapped[str] = mapped_column(nullable=False)

    booking: Mapped[list["Bookings"]] = relationship(back_populates="user")

    def __str__(self):
        return f"User: {self.email}"
