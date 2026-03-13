from pydantic import BaseModel
from typing import Literal

class EventCreate(BaseModel):
    event_type: Literal["view", "cart", "purchase"]
    product_id: int
    user_session: str

class EventOut(EventCreate):
    event_id: int
    event_time: str
    user_id: int

    class Config:
        from_attributes = True

