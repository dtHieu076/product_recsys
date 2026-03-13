from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from ..models.product import Product
from ..schemas.product import ProductOut
from typing import List

async def get_products(db: AsyncSession, skip: int = 0, limit: int = 100) -> List[ProductOut]:
    stmt = select(Product).offset(skip).limit(limit)
    result = await db.execute(stmt)
    products = result.scalars().all()
    return products

