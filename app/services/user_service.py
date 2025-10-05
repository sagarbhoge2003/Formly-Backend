from asyncpg.connection import Connection
from app.models.user import UserSignUp, UserResponse
from app.core.security import hash_password
from app.core.exceptions import UserAlreadyExistsException
from app.repositories.user_repo import find_user_by_email, insert_user


async def signup_user(conn: Connection, user: UserSignUp) -> UserResponse:
    existing_user = await find_user_by_email(conn, user.email)
    if existing_user:
        raise UserAlreadyExistsException()

    hashed_password = hash_password(user.password)
    new_user = await insert_user(conn, user, hashed_password)
    return UserResponse(**new_user)