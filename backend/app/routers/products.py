from fastapi import APIRouter, Depends, HTTPException
from typing import Literal
from sqlalchemy.ext.asyncio import AsyncSession
from ..database import get_db
from ..services.product_service import get_products
from ..services.event_service import create_event
from ..services.rec_service import get_recommendations
from ..schemas.product import ProductOut
from ..schemas.event import EventCreate
from ..schemas.rec import RecOut
from ..core.security import get_current_user
from ..models.user import User
from ..models.product import Product

router = APIRouter(prefix="/products", tags=["products"])

@router.get("/", response_model=list[ProductOut])
async def read_products(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    products = await get_products(db, skip=skip, limit=limit)
    return products

@router.post("/{product_id}/{event_type}")
async def track_event(
    product_id: int,
    event_type: Literal["view", "cart", "purchase"],
    user_session: str,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    # Check product exists
    stmt = select(Product).where(Product.product_id == product_id)
    result = await db.execute(stmt)
    product = result.scalar_one_or_none()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    event = await create_event(db, event_type, product_id, current_user.user_id, user_session)
    return {"event_id": event.event_id, "message": f"{event_type} tracked"}

@router.get("/recs", response_model=RecOut)
async def read_recs(current_user: User = Depends(get_current_user)):
    recs = await get_recommendations(current_user.user_id)
    return recs

