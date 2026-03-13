from pydantic import BaseModel
from typing import List
from .product_response import ProductResponse

class RecResponse(BaseModel):
    recommendations: List[ProductResponse]

