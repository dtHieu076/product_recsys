from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from ..entities.user import User

async def get_user(db: AsyncSession, username: str):
    stmt = select(User).where(User.username == username)
    result = await db.execute(stmt)
    return result.scalar_one_or_none()

async def get_user_by_id(db: AsyncSession, user_id: int):
    stmt = select(User).where(User.user_id == user_id)
    result = await db.execute(stmt)
    return result.scalar_one_or_none()

