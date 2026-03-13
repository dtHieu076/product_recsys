from pydantic import BaseModel, Field
from typing import Optional
from pydantic import Field

class UserBase(BaseModel):
    username: str = Field(..., min_length=1, max_length=50)

class UserCreateRequest(UserBase):
    password: str

class UserLoginRequest(UserBase):
    password: str

