from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Incident, Room, User
from schemas import IncidentRequest, IncidentResponse
from auth import get_current_user, require_admin

router = APIRouter(prefix="/incidents", tags=["Incidentes"])


@router.post("", response_model=IncidentResponse, status_code=201,
             summary="Abrir incidente")
def open_incident(
    body: IncidentRequest,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    if not db.query(Room).filter(Room.id == body.room_id).first():
        raise HTTPException(status_code=404, detail="Sala não encontrada.")

    incident = Incident(
        room_id=body.room_id,
        reported_by=user.email,
        description=body.description,
        status="OPEN",
    )
    db.add(incident)
    db.commit()
    db.refresh(incident)
    return incident


@router.patch("/{incident_id}/close", response_model=IncidentResponse,
              summary="Fechar incidente (apenas ADMIN)")
def close_incident(
    incident_id: int,
    db: Session = Depends(get_db),
    user: User = Depends(require_admin),
):
    incident = db.query(Incident).filter(Incident.id == incident_id).first()
    if not incident:
        raise HTTPException(status_code=404, detail="Incidente não encontrado.")
    if incident.status != "OPEN":
        raise HTTPException(status_code=400, detail="Incidente já está fechado.")

    incident.status = "CLOSED"
    db.commit()
    db.refresh(incident)
    return incident
