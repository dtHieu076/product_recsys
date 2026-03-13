from sqlalchemy.ext.asyncio import AsyncSession
from ..repositories.event_repo import create_event
from ..dtos.event_response import EventResponse
from ..entities.event import ActionType

async def create_event(db: AsyncSession, event_type: str, product_id: int, user_id: int, user_session: str) -> EventResponse:
    event = await create_event(db, event_type, product_id, user_id, user_session)
    return event

