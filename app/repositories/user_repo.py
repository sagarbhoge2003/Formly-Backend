from asyncpg.connection import Connection
from typing import Optional
from app.models.user import UserSignUp, User
from app.logger import logger

class UserRepository:
    def __init__(self, conn: Connection):
        self.conn = conn

    async def find_by_email(self, email: str) -> Optional[User]:
        query = """
        SELECT id, first_name, last_name, username, email, password_hash
        FROM users
        WHERE email = $1
        """
        result = await self.conn.fetchrow(query, email)
        if result:
            return User.from_db_record(result)
        return None

    async def insert_user(self, user: UserSignUp, hashed_password: str) -> User:
        query = """
        INSERT INTO users (first_name, last_name, username, email, password_hash)
        VALUES ($1, $2, $3, $4, $5)
        RETURNING id, first_name, last_name, username, email, password_hash;
        """
        result = await self.conn.fetchrow(
            query,
            user.first_name,
            user.last_name,
            user.username,
            user.email,
            hashed_password
        )
        return User.from_db_record(result)
