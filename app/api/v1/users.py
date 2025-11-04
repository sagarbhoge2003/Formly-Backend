from fastapi import APIRouter, Depends
from app.models.user import UserSignUp, UserLogin, UserResponse, Token
from app.services.user_service import UserService
from app.core.dependencies import get_user_service

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/signup", response_model=UserResponse)
async def signup(user: UserSignUp, user_service: UserService = Depends(get_user_service)):
    created_user = await user_service.signup_user(user)  # <-- updated
    return created_user

@router.post("/login", response_model=Token)
async def login(credentials: UserLogin, user_service: UserService = Depends(get_user_service)):
    token_data = await user_service.login_user(credentials)  # <-- updated
    return token_data

@router.get("/me")
async def me():
    return {"message": "This is a test route"}
