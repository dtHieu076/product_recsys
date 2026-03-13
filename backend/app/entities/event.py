from sqlalchemy import BigInteger, TIMESTAMP, String, ForeignKey, Column, text
from sqlalchemy.types import Enum
from ...database import Base
import enum

class ActionType(str, enum.Enum):
    view = "view"
    cart = "cart"
    purchase = "purchase"

class Event(Base):
    __tablename__ = "events"

    event_id = Column(BigInteger, primary_key=True)
    event_time = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))
    event_type = Column(Enum(ActionType))
    product_id = Column(BigInteger, ForeignKey("products.product_id"))
    user_id = Column(BigInteger, ForeignKey("users.user_id"))
    user_session = Column(String(255))

