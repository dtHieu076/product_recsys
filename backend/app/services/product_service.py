from sqlalchemy.ext.asyncio import AsyncSession
from ..repositories.product_repo import get_products
from ..dtos.product_response import ProductResponse
from typing import List

async def get_products(db: AsyncSession, skip: int = 0, limit: int = 100) -> List[ProductResponse]:
    products = await get_products(db, skip, limit)
    return products

