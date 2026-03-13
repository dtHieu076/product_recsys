from sqlalchemy import BigInteger, String, Numeric, ForeignKey, Column
from ...database import Base

class Category(Base):
    __tablename__ = "categories"
    category_id = Column(BigInteger, primary_key=True)
    category_code = Column(String(255))

class Product(Base):
    __tablename__ = "products"

    product_id = Column(BigInteger, primary_key=True)
    category_id = Column(BigInteger, ForeignKey("categories.category_id"))
    brand = Column(String(100))
    price = Column(Numeric(10,2))
    product_name = Column(String(255))
    image_url = Column(String(255))

