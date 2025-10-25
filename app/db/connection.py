import asyncpg
from typing import Optional
from app.core.config import settings
from app.logger import logger

# Global connection pool
_pool: Optional[asyncpg.Pool] = None

async def get_pool() -> asyncpg.Pool:
    """Get the global connection pool, creating it if it doesn't exist."""
    global _pool
    if _pool is None:
        _pool = await asyncpg.create_pool(
            settings.db_dsn,
            min_size=5,  # Minimum connections in pool
            max_size=20,  # Maximum connections in pool
            command_timeout=60,  # Command timeout in seconds
        )
        logger.info("Database connection pool created")
    return _pool

async def get_db():
    """Get a connection from the pool."""
    pool = await get_pool()
    async with pool.acquire() as conn:
        yield conn

async def close_pool():
    """Close the connection pool."""
    global _pool
    if _pool is not None:
        await _pool.close()
        _pool = None
        logger.info("Database connection pool closed")

async def test_db_connection():
    """Try to connect to the database and run a simple query."""
    try:
        pool = await get_pool()
        async with pool.acquire() as conn:
            await conn.execute("SELECT 1;")
        return True
    except Exception as e:
        logger.error(f"Database connection failed: {e}")
        return False
