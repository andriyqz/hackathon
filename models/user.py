from sqlalchemy import Column, Integer, String, Enum, DateTime
from datetime import datetime
from db.base import Base
from .enums import UserRole


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)

    role = Column(Enum(UserRole), nullable=False)

    created_at = Column(DateTime, default=datetime.now(datetime.UTC))