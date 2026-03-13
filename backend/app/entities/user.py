from sqlalchemy import BigInteger, String, Column
from ..database import Base

class User(Base):
    __tablename__ = "users"

    user_id = Column(BigInteger, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    password = Column(String(255), nullable=False)

