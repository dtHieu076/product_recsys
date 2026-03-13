from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from ..entities.product import Product
from typing import List

async def get_products(db: AsyncSession, skip: int = 0, limit: int = 100) -> List[Product]:
    stmt = select(Product).offset(skip).limit(limit)
    result = await db.execute(stmt)
    return result.scalars().all()

async def get_product(db: AsyncSession, product_id: int):
    stmt = select(Product).where(Product.product_id == product_id)
    result = await db.execute(stmt)
    return result.scalar_one_or_none()

