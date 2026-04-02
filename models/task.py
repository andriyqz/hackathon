from sqlalchemy import Column, Integer, ForeignKey, Enum, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from db.base import Base
from .enums import TaskStatus, Priority


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)

    request_id = Column(Integer, ForeignKey("requests.id"))
    driver_id = Column(Integer, ForeignKey("users.id"))

    status = Column(Enum(TaskStatus), default=TaskStatus.ASSIGNED)
    
    assigned_at = Column(DateTime, default=datetime.now(datetime.UTC))
    completed_at = Column(DateTime)

    request = relationship("Request", back_populates="tasks")
    driver = relationship("User")

