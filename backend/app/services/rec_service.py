# Dummy rec service - replace with ALS later
from typing import List
from ..schemas.product import ProductOut
from ..schemas.rec import RecOut

async def get_recommendations(user_id: int, n: int = 5) -> RecOut:
    # Mock recs - product_ids from DB sample
    mock_products = [
        ProductOut(product_id=1004249, category_id=None, brand="apple", price=739.32, product_name="Apple iPhone 11", image_url="iphone11.jpg"),
        ProductOut(product_id=1005115, category_id=None, brand="apple", price=949.15, product_name="Apple iPhone 12 Pro", image_url="iphone12.jpg"),
        ProductOut(product_id=1004856, category_id=None, brand="xiaomi", price=130.76, product_name="Xiaomi Redmi Note 9", image_url="redmi9.jpg"),
    ]
    return RecOut(recommendations=mock_products[:n])

