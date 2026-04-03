from fastapi import APIRouter, Depends, Query
from fastapi import Body

from sqlalchemy.orm import Session

from typing import List, Optional

from repositories.filters import BaseFilter, EqualsFilter, GreaterThanFilter, LessThanFilter, apply_filters
from services.request_service import RequestService
from schemas.request import RequestCreate, RequestResponse, RequestStatus
from models.enums import Priority
from core.dependencies import get_db

router = APIRouter()

def get_request_service(db: Session = Depends(get_db)):
    return RequestService(db=db)


@router.get('/', response_model=List[RequestResponse])
def get_requests(
    request_service: RequestService = Depends(get_request_service),
    status: Optional[RequestStatus] = Query(None),
    min_id: Optional[int] = Query(None),
    max_id: Optional[int] = Query(None),
    priority: Optional[Priority] = Query(None)
):
    mapping = {
        "status": {"class": EqualsFilter, "field": "status"},
        "min_id": {"class": GreaterThanFilter, "field": "id"},
        "max_id": {"class": LessThanFilter, "field": "id"},
        "priority": {"class": EqualsFilter, "field": "priority"}
    }
    
    params = {
        "status": status,
        "min_id": min_id,
        "max_id": max_id,
        "priority": priority
    }
    
    filters = apply_filters(params, mapping)
    return request_service.get_requests(filters=filters)


@router.post('/', response_model=RequestResponse)
def create_request(user_id: int, request_data:  RequestCreate = Body(...), 
                   request_service: RequestService = Depends(get_request_service)):
    return request_service.create_request(user_id=user_id, data=request_data)