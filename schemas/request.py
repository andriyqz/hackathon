from pydantic import BaseModel
from datetime import datetime
from models.enums import RequestStatus, Priority

class RequestCreate(BaseModel):
    to_location: str
    priority: Priority
    description: str
    


class RequestResponse(BaseModel):
    id: int
    to_location: str
    description: str
    priority: Priority
    status: RequestStatus
    created_at: datetime

    class Config:
        from_attributes = True