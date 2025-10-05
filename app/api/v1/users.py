from fastapi import APIRouter, Depends
from asyncpg.connection import Connection
from app.models.user import UserSignUp, UserResponse
from app.services.user_service import signup_user
from app.db.connection import get_db

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/signup", response_model=UserResponse)
async def signup(user: UserSignUp, conn: Connection = Depends(get_db)):
    return await signup_user(conn, user)