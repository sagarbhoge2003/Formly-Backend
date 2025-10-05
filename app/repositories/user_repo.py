from asyncpg.connection import Connection
from app.models.user import UserSignUp


async def find_user_by_email(conn: Connection, email: str):
    return await conn.fetchrow("SELECT * FROM users WHERE email = $1", email)


async def insert_user(conn: Connection, user: UserSignUp, hashed_password: str):
    query = """
    INSERT INTO users (username, email, password)
    VALUES ($1, $2, $3)
    RETURNING id, username, email;
    """
    return await conn.fetchrow(query, user.username, user.email, hashed_password)