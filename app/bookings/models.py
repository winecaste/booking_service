from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, ForeignKey, Computed
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import date

from app.database import Base

if TYPE_CHECKING:
    from app.users.models import Users
    from app.hotels.rooms.models import Rooms


class Bookings(Base):
    __tablename__ = "bookings"

    id: Mapped[int] = mapped_column(primary_key=True)
    room_id: Mapped[int] = mapped_column(ForeignKey("rooms.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    date_from: Mapped[date] = mapped_column(nullable=False)
    date_to: Mapped[date] = mapped_column(nullable=False)
    price: Mapped[int] = mapped_column(nullable=False)
    total_cost = Column(Integer, Computed("(date_to - date_from) * price"))
    total_days = Column(Integer, Computed("date_to - date_from"))

    user: Mapped["Users"] = relationship(back_populates="booking")
    room: Mapped["Rooms"] = relationship(back_populates="booking")

    def __str__(self):
        return f"Booking #{self.id}"
