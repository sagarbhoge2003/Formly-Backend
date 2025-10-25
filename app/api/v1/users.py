from fastapi import APIRouter, Depends
from asyncpg.connection import Connection
from app.models.user import UserSignUp, UserResponse, UserLogin, Token
from app.core.dependencies import get_user_service,get_user_repository
from app.services.user_service import UserService

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/signup", response_model=UserResponse)
async def signup(user: UserSignUp, service: UserService = Depends(get_user_service)):
    return await service.signup_user(user)

@router.post("/login", response_model=Token)
async def login(user: UserLogin, service: UserService = Depends(get_user_service)):
    return await service.login_user(user)