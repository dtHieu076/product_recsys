from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from ..models.event import Event, ActionType
from ..schemas.event import EventCreate, EventOut
from typing import Dict

async def create_event(db: AsyncSession, event_type: str, product_id: int, user_id: int, user_session: str) -> EventOut:
    event = Event(
        event_type=ActionType(event_type),
        product_id=product_id,
        user_id=user_id,
        user_session=user_session
    )
    db.add(event)
    await db.commit()
    await db.refresh(event)
    return event

