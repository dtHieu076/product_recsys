from pydantic import BaseModel
from typing import List
from ..schemas.product import ProductOut

class RecOut(BaseModel):
    recommendations: List[ProductOut]

