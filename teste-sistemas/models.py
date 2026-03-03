from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = "users"

    id       = Column(Integer, primary_key=True, index=True)
    name     = Column(String, nullable=False)
    email    = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    role     = Column(String, nullable=False, default="USER")  # ADMIN | USER

    tokens   = relationship("Token", back_populates="user")


class Token(Base):
    __tablename__ = "tokens"

    id    = Column(Integer, primary_key=True, index=True)
    token = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, ForeignKey("users.email"), nullable=False)

    user  = relationship("User", back_populates="tokens")


class Room(Base):
    __tablename__ = "rooms"

    id        = Column(Integer, primary_key=True, index=True)
    name      = Column(String, unique=True, nullable=False)
    capacity  = Column(Integer, nullable=False)
    resources = Column(String, nullable=False, default="")  # CSV: "projetor,ar-condicionado"


class Booking(Base):
    __tablename__ = "bookings"

    id         = Column(Integer, primary_key=True, index=True)
    room_id    = Column(Integer, ForeignKey("rooms.id"), nullable=False)
    user_email = Column(String, ForeignKey("users.email"), nullable=False)
    date       = Column(String, nullable=False)        # YYYY-MM-DD
    start_time = Column(String, nullable=False)        # HH:MM
    end_time   = Column(String, nullable=False)        # HH:MM
    purpose    = Column(String, nullable=False)
    status     = Column(String, nullable=False, default="CONFIRMED")


class Incident(Base):
    __tablename__ = "incidents"

    id          = Column(Integer, primary_key=True, index=True)
    room_id     = Column(Integer, ForeignKey("rooms.id"), nullable=False)
    reported_by = Column(String, ForeignKey("users.email"), nullable=False)
    description = Column(String, nullable=False)
    status      = Column(String, nullable=False, default="OPEN")  # OPEN | CLOSED
