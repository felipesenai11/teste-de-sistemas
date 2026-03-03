import uuid
from fastapi import Header, HTTPException, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Token, User


def generate_token() -> str:
    return str(uuid.uuid4())


def get_current_user(
    authorization: str = Header(..., description="Bearer {token}"),
    db: Session = Depends(get_db),
) -> User:
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Token inválido ou ausente.")

    raw_token = authorization.split(" ", 1)[1]
    token_row = db.query(Token).filter(Token.token == raw_token).first()

    if not token_row:
        raise HTTPException(status_code=401, detail="Token inválido ou expirado.")

    user = db.query(User).filter(User.email == token_row.email).first()
    if not user:
        raise HTTPException(status_code=401, detail="Usuário não encontrado.")

    return user


def require_admin(
    user: User = Depends(get_current_user),
) -> User:
    if user.role != "ADMIN":
        raise HTTPException(status_code=403, detail="Acesso restrito a administradores.")
    return user
