from fastapi import APIRouter
from .endpoints import tasks, requests

api_router = APIRouter()

api_router.include_router(tasks.router, prefix="/tasks", tags=["tasks"])
api_router.include_router(requests.router, prefix="/requests", tags=["requests"])