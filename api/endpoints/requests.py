from fastapi import APIRouter, Depends
from fastapi import Body
from sqlalchemy.orm import Session

from typing import List

from models import User
from services.request_service import RequestService
from schemas.request import RequestCreate, RequestResponse
from core.dependencies import get_current_user, get_db

router = APIRouter()

def get_request_service(db: Session = Depends(get_db)):
    return RequestService(db=db)


@router.get('/', response_model=List[RequestResponse])
def get_requests(request_service: RequestService = Depends(get_request_service)):
    return request_service.get_new_requests()


@router.post('/', response_model=RequestResponse)
def create_request(request_data: RequestCreate = Body(...),
                   current_user: User = Depends(get_current_user),
                   request_service: RequestService = Depends(get_request_service)):
    return request_service.create_request(user_id=current_user.id, data=request_data)
