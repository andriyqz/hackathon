from models import Request
from models.enums import RequestStatus

from typing import List
from .filters import BaseFilter, EqualsFilter, GreaterThanFilter, LessThanFilter

class RequestRepository:

    def __init__(self, db):
        self.db = db

    def create(self, request: Request):
        self.db.add(request)
        self.db.commit()
        self.db.refresh(request)
        return request
    
    def get(self, filters: List[BaseFilter]=None):
        query = self.db.query(Request)
    
        if filters:
            for f in filters:
                query = f.apply(Request, query)

        return query.all()

    def update(self, request: Request):
        self.db.commit()
        self.db.refresh(request)
        return request