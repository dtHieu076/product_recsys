from pydantic import BaseModel, Field
from typing import Optional
from ..models.user import User

class UserBase(BaseModel):
    username: str = Field(..., min_length=1, max_length=50)

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    user_id: int

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

