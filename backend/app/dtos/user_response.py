from pydantic import BaseModel
from typing import Optional
from ..entities.user import User

class UserResponse(BaseModel):
    user_id: int
    username: str

    class Config:
        from_attributes = True

