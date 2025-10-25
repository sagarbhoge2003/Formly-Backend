import asyncio
import sys
from fastapi import FastAPI
from app.core.config import settings
from app.db.connection import test_db_connection, close_pool
from app.middleware import LoggingMiddleware
from app.api.v1.users import router as users_router
from app.logger import logger


def create_app() -> FastAPI:
    app = FastAPI(title=settings.PROJECT_NAME)

    # Add middleware
    app.add_middleware(LoggingMiddleware)

    # Include routers
    app.include_router(users_router)

    @app.get("/", tags=["health"])
    async def root():
        return {"message": f"{settings.PROJECT_NAME} is running!"}

    @app.on_event("startup")
    async def startup_event():
        """Initialize database connection pool on startup."""
        logger.info("Initializing database connection pool...")
        ok = await test_db_connection()
        if not ok:
            logger.error("Cannot start FastAPI — Database connection failed!")
            sys.exit(1)
        logger.info("Database connection pool initialized successfully!")

    @app.on_event("shutdown")
    async def shutdown_event():
        """Close database connection pool on shutdown."""
        logger.info("Closing database connection pool...")
        await close_pool()
        logger.info("Database connection pool closed successfully!")

    return app


app = create_app()
