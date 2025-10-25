from asyncpg.connection import Connection
from app.models.user import UserSignUp, UserResponse, UserLogin, Token, User
from app.core.security import hash_password, verify_password, create_access_token
from app.core.exceptions import UserAlreadyExistsException, InvalidCredentialsException
from app.repositories.user_repo import UserRepository
from app.logger import logger


class UserService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    async def signup_user(self, user: UserSignUp) -> UserResponse:        
        # Check if user exists by email
        existing_user = await self.repo.find_by_email(user.email)
        if existing_user:
            logger.warning(f"User already exists with email: {user.email}")
            raise UserAlreadyExistsException()

        hashed_password = hash_password(user.password)
        new_user = await self.repo.insert_user(user, hashed_password)
        
        # Convert domain model to response model
        return new_user.to_response()

    async def login_user(self, user: UserLogin) -> Token:
        existing_user = await self.repo.find_by_email(user.email)
        if not existing_user:
            raise InvalidCredentialsException()

        # Check password against password_hash from domain model
        if not verify_password(user.password, existing_user.password_hash):
            raise InvalidCredentialsException()

        access_token = create_access_token({"sub": str(existing_user.id)})
        return Token(access_token=access_token)