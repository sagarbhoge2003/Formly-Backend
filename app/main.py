from fastapi import FastAPI

from .middleware import LoggingMiddleware


# -----------------------------
# FastAPI app setup
# -----------------------------
app = FastAPI(title="FastAPI Backend with Logging")

# Add middleware
app.add_middleware(LoggingMiddleware)


@app.get("/", tags=["health"])
def root():
    return {"message": "FastAPI Backend is running !!!"}


@app.get("/users", tags=["user"])
def get_users():
    return {"users": ["alice", "bob"]}
