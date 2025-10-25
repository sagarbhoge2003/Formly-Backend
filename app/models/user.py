from pydantic import BaseModel, EmailStr, constr
from typing import Optional
from uuid import UUID


class UserSignUp(BaseModel):
    first_name: constr(min_length=1, max_length=100)
    last_name: Optional[constr(max_length=100)] = None
    username: constr(min_length=3, max_length=50)
    email: EmailStr
    password: constr(min_length=6)


class UserResponse(BaseModel):
    id: UUID
    first_name: str
    last_name: Optional[str] = None
    username: str
    email: EmailStr


class UserLogin(BaseModel):
    email: EmailStr
    password: constr(min_length=6)


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


# Domain model for repository operations
class User(BaseModel):
    id: UUID
    first_name: str
    last_name: Optional[str] = None
    username: str
    email: EmailStr
    password_hash: str

    @classmethod
    def from_db_record(cls, record) -> "User":
        """Create User instance from database record"""
        return cls(
            id=record["id"],
            first_name=record["first_name"],
            last_name=record["last_name"],
            username=record["username"],
            email=record["email"],
            password_hash=record["password_hash"]
        )

    def to_response(self) -> UserResponse:
        """Convert User domain model to UserResponse"""
        return UserResponse(
            id=self.id,
            first_name=self.first_name,
            last_name=self.last_name,
            username=self.username,
            email=self.email
        )