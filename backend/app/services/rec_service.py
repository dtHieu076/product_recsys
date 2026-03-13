# Dummy rec service - replace with ALS later
from typing import List
from ..dtos.product_response import ProductResponse
from ..dtos.rec_response import RecResponse

async def get_recommendations(user_id: int, n: int = 5) -> RecResponse:
    # Mock recs
    mock_products = [
        ProductResponse(product_id=1004249, category_id=None, brand="apple", price=739.32, product_name="Apple iPhone 11", image_url="iphone11.jpg"),
        ProductResponse(product_id=1005115, category_id=None, brand="apple", price=949.15, product_name="Apple iPhone 12 Pro", image_url="iphone12.jpg"),
        ProductResponse(product_id=1004856, category_id=None, brand="xiaomi", price=130.76, product_name="Xiaomi Redmi Note 9", image_url="redmi9.jpg"),
    ]
    return RecResponse(recommendations=mock_products[:n])

