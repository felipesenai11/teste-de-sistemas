from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from models import Booking, Room, User
from schemas import BookingRequest, BookingResponse
from auth import get_current_user

router = APIRouter(prefix="/bookings", tags=["Reservas"])


def has_conflict(db: Session, room_id: int, date: str, start: str, end: str) -> bool:
    existing = db.query(Booking).filter(
        Booking.room_id == room_id,
        Booking.date == date,
    ).all()
    for b in existing:
        if start < b.end_time and end > b.start_time:
            return True
    return False


@router.post("", response_model=BookingResponse, status_code=201,
             summary="Criar reserva")
def create_booking(
    body: BookingRequest,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    if not db.query(Room).filter(Room.id == body.room_id).first():
        raise HTTPException(status_code=404, detail="Sala não encontrada.")

    if has_conflict(db, body.room_id, body.date, body.start_time, body.end_time):
        raise HTTPException(status_code=409, detail="Conflito de horário para esta sala.")

    booking = Booking(
        room_id=body.room_id,
        user_email=user.email,
        date=body.date,
        start_time=body.start_time,
        end_time=body.end_time,
        purpose=body.purpose,
        status="CONFIRMED",
    )
    db.add(booking)
    db.commit()
    db.refresh(booking)
    return booking


@router.get("/my", response_model=List[BookingResponse],
            summary="Listar minhas reservas")
def my_bookings(
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    return db.query(Booking).filter(Booking.user_email == user.email).all()
