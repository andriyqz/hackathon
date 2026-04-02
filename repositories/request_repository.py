from models import Request
from models.enums import RequestStatus


class RequestRepository:

    def __init__(self, db):
        self.db = db

    def create(self, request: Request):
        self.db.add(request)
        self.db.commit()
        self.db.refresh(request)
        return request
    
    def get_by_id(self, request_id: int):
        return self.db.query(Request).filter(
            Request.id == request_id
        ).first()
    
    def get_by_status(self, status: RequestStatus):
        return self.db.query(Request).filter(
            Request.status == status
        ).all()
    
    def update(self, request: Request):
        self.db.commit()
        self.db.refresh(request)
        return request