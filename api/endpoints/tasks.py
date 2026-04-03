from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from services.task_service import TaskService
from core.dependencies import get_db

router = APIRouter()

def get_task_service(db: Session = Depends(get_db)):
    return TaskService(db=db)

# @router.get('/')
# def get_tasks(task_service: TaskService = Depends(get_task_service)):
#     return task_service.