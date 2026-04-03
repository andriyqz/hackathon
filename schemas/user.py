from pydantic import BaseModel, EmailStr
from datetime import datetime
from models.enums import UserRole


class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    password: str
    role: UserRole


class UserResponse(UserBase):
    id: int
    role: UserRole
    created_at: datetime

    class Config:
        from_attributes = True


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
