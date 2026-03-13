from sqlalchemy.ext.asyncio import AsyncSession
from ..entities.event import Event
from ..entities.product import Product
from sqlalchemy import select

async def create_event(db: AsyncSession, event_type: str, product_id: int, user_id: int, user_session: str, event: Event = None):
    if event is None:
        event = Event(
            event_type=event_type,
            product_id=product_id,
            user_id=user_id,
            user_session=user_session
        )
    db.add(event)
    await db.commit()
    await db.refresh(event)
    return event

