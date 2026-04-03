from fastapi import APIRouter
from .endpoints import auth, tasks, requests

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(requests.router, prefix="/requests", tags=["requests"])