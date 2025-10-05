import time
import uuid
from typing import List

from fastapi import Request, Response
from fastapi.routing import APIRoute
from starlette.middleware.base import BaseHTTPMiddleware

from .logger import _request_id_ctx_var, logger


# -----------------------------
# Logging Middleware
# -----------------------------
class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()

        # Set or generate request_id
        request_id = request.headers.get("X-Request-ID", str(uuid.uuid4()))
        _request_id_ctx_var.set(request_id)

        try:
            response: Response = await call_next(request)
        except Exception as e:
            logger.exception(f"{request.method} {request.url.path} failed: {e}")
            raise

        # Add request_id in response header
        response.headers["X-Request-ID"] = request_id

        # Get route tags if available
        route: APIRoute = request.scope.get("route")
        tags: List[str] = []
        if isinstance(route, APIRoute):
            tags = route.tags or []

        process_time = (time.time() - start_time) * 1000
        logger.info(
            f"{request.method} {request.url.path} "
            f"[tags={tags}] "
            f"status={response.status_code} "
            f"time={process_time:.2f}ms"
        )

        return response
