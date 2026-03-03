from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from models import Room, User
from schemas import RoomRequest, RoomResponse
from auth import get_current_user, require_admin

router = APIRouter(prefix="/rooms", tags=["Salas"])


@router.post("", response_model=RoomResponse, status_code=201,
             summary="Criar sala (apenas ADMIN)")
def create_room(
    body: RoomRequest,
    db: Session = Depends(get_db),
    user: User = Depends(require_admin),
):
    if db.query(Room).filter(Room.name == body.name).first():
        raise HTTPException(status_code=400, detail="Nome da sala já existe.")

    room = Room(
        name=body.name,
        capacity=body.capacity,
        resources=",".join(body.resources),  # salva como CSV
    )
    db.add(room)
    db.commit()
    db.refresh(room)
    return room


@router.get("", response_model=List[RoomResponse], summary="Listar todas as salas")
def list_rooms(
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    return db.query(Room).all()
