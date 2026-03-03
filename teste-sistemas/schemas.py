from pydantic import BaseModel, field_validator, model_validator, EmailStr
from typing import List, Optional
from enum import Enum
import re


class Role(str, Enum):
    ADMIN = "ADMIN"
    USER  = "USER"


# ──────────────────────────────────────────
# AUTH
# ──────────────────────────────────────────
class RegisterRequest(BaseModel):
    name:     str
    email:    EmailStr
    password: str
    role:     Role = Role.USER

    @field_validator("password")
    @classmethod
    def password_rules(cls, v):
        if len(v) < 8:
            raise ValueError("Senha deve ter no mínimo 8 caracteres.")
        if not re.search(r"[a-zA-Z]", v):
            raise ValueError("Senha deve conter pelo menos 1 letra.")
        if not re.search(r"\d", v):
            raise ValueError("Senha deve conter pelo menos 1 número.")
        return v


class RegisterResponse(BaseModel):
    id:      int
    name:    str
    email:   str
    role:    str

    model_config = {"from_attributes": True}


class LoginRequest(BaseModel):
    email:    EmailStr
    password: str


class LoginResponse(BaseModel):
    token: str
    role:  str


# ──────────────────────────────────────────
# ROOMS
# ──────────────────────────────────────────
class RoomRequest(BaseModel):
    name:      str
    capacity:  int
    resources: List[str] = []

    @field_validator("capacity")
    @classmethod
    def capacity_positive(cls, v):
        if v <= 0:
            raise ValueError("Capacidade deve ser maior que 0.")
        return v


class RoomResponse(BaseModel):
    id:        int
    name:      str
    capacity:  int
    resources: List[str]

    model_config = {"from_attributes": True}

    @field_validator("resources", mode="before")
    @classmethod
    def parse_resources(cls, v):
        # Converte CSV → lista quando vier do banco
        if isinstance(v, str):
            return [r.strip() for r in v.split(",") if r.strip()]
        return v


# ──────────────────────────────────────────
# BOOKINGS
# ──────────────────────────────────────────
class BookingRequest(BaseModel):
    room_id:    int
    date:       str   # YYYY-MM-DD
    start_time: str   # HH:MM
    end_time:   str   # HH:MM
    purpose:    str

    @model_validator(mode="after")
    def validate_times(self):
        if self.start_time >= self.end_time:
            raise ValueError("Hora de início deve ser menor que hora de término.")
        if self.start_time < "08:00" or self.end_time > "22:00":
            raise ValueError("Reservas permitidas apenas entre 08:00 e 22:00.")
        return self


class BookingResponse(BaseModel):
    id:         int
    room_id:    int
    user_email: str
    date:       str
    start_time: str
    end_time:   str
    purpose:    str
    status:     str

    model_config = {"from_attributes": True}


# ──────────────────────────────────────────
# INCIDENTS
# ──────────────────────────────────────────
class IncidentRequest(BaseModel):
    room_id:     int
    description: str

    @field_validator("description")
    @classmethod
    def description_min_length(cls, v):
        if len(v) < 10:
            raise ValueError("Descrição deve ter no mínimo 10 caracteres.")
        return v


class IncidentResponse(BaseModel):
    id:          int
    room_id:     int
    reported_by: str
    description: str
    status:      str

    model_config = {"from_attributes": True}
