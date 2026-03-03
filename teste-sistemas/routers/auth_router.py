from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import User, Token
from schemas import RegisterRequest, RegisterResponse, LoginRequest, LoginResponse
from auth import generate_token

router = APIRouter(prefix="/auth", tags=["Autenticação"])


@router.post("/register", response_model=RegisterResponse, status_code=201,
             summary="Registrar novo usuário")
def register(body: RegisterRequest, db: Session = Depends(get_db)):
    if db.query(User).filter(User.email == body.email).first():
        raise HTTPException(status_code=400, detail="Email já cadastrado.")

    user = User(
        name=body.name,
        email=body.email,
        password=body.password,   # sala de aula: sem hash
        role=body.role.value,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@router.post("/login", response_model=LoginResponse, summary="Login e obtenção de token")
def login(body: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == body.email).first()
    if not user or user.password != body.password:
        raise HTTPException(status_code=401, detail="Email ou senha inválidos.")

    token_value = generate_token()
    db.add(Token(token=token_value, email=user.email))
    db.commit()

    return {"token": token_value, "role": user.role}
