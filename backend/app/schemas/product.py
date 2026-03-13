from pydantic import BaseModel
from typing import Optional
from decimal import Decimal

class ProductOut(BaseModel):
    product_id: int
    category_id: Optional[int]
    brand: Optional[str]
    price: Decimal
    product_name: str
    image_url: Optional[str]

    class Config:
        from_attributes = True

