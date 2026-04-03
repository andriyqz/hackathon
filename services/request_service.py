from models import Request
from models.enums import RequestStatus
from sqlalchemy.orm import Session
from repositories.request_repository import RequestRepository


class RequestService:
    
    def __init__(self, db: Session):
        self.db = db
        self.__request_repo = RequestRepository(db=db)

    def create_request(self, user_id: int, data):
        request = Request(
            created_by=user_id,
            to_location=data.to_location,
            description=data.description,
            status=RequestStatus.NEW,
            priority=data.priority
        )

        self.__request_repo.create(request=request)

        return request

    def get_new_requests(self):
        return self.__request_repo.get_by_status(status=RequestStatus.NEW)
    
    
