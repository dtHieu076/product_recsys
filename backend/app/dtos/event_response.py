from pydantic import BaseModel
from typing import Optional
from ..entities.event import Event

class EventResponse(BaseModel):
    event_id: int
    event_type: str
    event_time: str
    product_id: int
    user_id: int
    user_session: str

    class Config:
        from_attributes = True

