from fastapi import APIRouter, Depends
from asyncpg.connection import Connection
from app.models.user import UserSignUp, UserResponse, UserLogin, Token
from app.core.dependencies import get_user_service,get_user_repository
from app.services.user_service import UserService


router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/signup")
async def signup():
    return {"message": "signup"}

@router.post("/login")
async def login():
    return {"message": "login"}

# Define a custom method
async def test():
    return {"message": "This is a Test"}

# Register the route manually with custom method
router.add_api_route(
    "/me",
    test,
    methods=["SAGAR"],  # custom HTTP method
    response_model=dict
)
