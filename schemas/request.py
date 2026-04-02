from pydantic import BaseModel
from datetime import datetime
from models.enums import RequestStatus

class RequestCreate(BaseModel):
    to_location: str
    description: str


class RequestResponse(BaseModel):
    id: int
    to_location: str
    description: str
    status: RequestStatus
    created_at: datetime

    class Config:
        from_attributes = True