# dependencies.py
from fastapi import Depends
from asyncpg.connection import Connection
from app.repositories.user_repo import UserRepository
from app.services.user_service import UserService
from app.db.connection import get_db

def get_user_repository(conn: Connection = Depends(get_db)) -> UserRepository:
    return UserRepository(conn)

def get_user_service(repo: UserRepository = Depends(get_user_repository)) -> UserService:
    return UserService(repo)