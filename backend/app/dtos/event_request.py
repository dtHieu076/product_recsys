from pydantic import BaseModel
from typing import Literal

class EventCreateRequest(BaseModel):
    event_type: Literal["view", "cart", "purchase"]
    product_id: int
    user_session: str

