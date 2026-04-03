from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import make_url

from core.config import settings
from .base import Base

url = make_url(settings.DATABASE_URL)
connect_args = {}

if url.get_backend_name() == "sqlite":
    connect_args = {"check_same_thread": False}

engine = create_engine(settings.DATABASE_URL, connect_args=connect_args, pool_pre_ping=False)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db():
    Base.metadata.create_all(bind=engine)