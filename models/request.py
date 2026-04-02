from sqlalchemy import Column, Integer, String, ForeignKey, Enum, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from db.base import Base
from .enums import RequestStatus, Priority


class Request(Base):
    __tablename__ = "requests"

    id = Column(Integer)
    
    created_by = Column(Integer, ForeignKey("users.id"))
    to_location = Column(String)
    status = Column(Enum(RequestStatus), default=RequestStatus.NEW)
    priority = Column(Enum(Priority), default=Priority.NORMAL)
    
    created_at = Column(DateTime, default=datetime.now(datetime.UTC))
    updated_at = Column(DateTime)

    creator = relationship("User")
    tasks = relationship("Task", back_populates="request")
