from sqlalchemy import Column, Integer, ForeignKey, Enum, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from db.base import Base
from .enums import TaskStatus, Priority


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)

    request_id = Column(Integer, ForeignKey("requests.id"))
    driver_id = Column(Integer, ForeignKey("users.id"))

    status = Column(Enum(TaskStatus), default=TaskStatus.ASSIGNED)
    
    assigned_at = Column(DateTime, default=datetime.now(timezone.utc))
    completed_at = Column(DateTime)

    request = relationship("Request", back_populates="tasks")
    driver = relationship("User")

