from pydantic import BaseModel
from datetime import datetime
from models.enums import TaskStatus


class TaskCreate(BaseModel):
    request_id: int
    driver_id: int


class TaskResponse(BaseModel):
    id: int
    request_id: int
    driver_id: int
    status: TaskStatus
    assigned_at: datetime

    class Config:
        from_attributes = True
