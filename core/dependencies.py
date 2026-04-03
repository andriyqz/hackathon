from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from models import User
from repositories.user_repository import UserRepository
from core.security import decode_access_token
from db.session import SessionLocal

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
    )

    try:
        payload = decode_access_token(token)
        user_id = payload.get("sub") or payload.get("user_id")
        user_id = int(user_id)
    except (TypeError, ValueError):
        raise credentials_exception

    user = UserRepository(db=db).get_by_id(user_id=user_id)
    if not user:
        raise credentials_exception

    return user
