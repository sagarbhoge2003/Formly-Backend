from pydantic import BaseModel, EmailStr, constr


class UserSignUp(BaseModel):
    username: constr(min_length=3, max_length=50)
    email: EmailStr
    password: constr(min_length=6)


class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
