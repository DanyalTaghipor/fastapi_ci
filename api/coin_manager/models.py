from sqlalchemy import Column, Integer, String, Float
from db.session import Base


class CoinManager(Base):
    __tablename__ = "coins"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    symbol = Column(String, index=True)
    price = Column(Float)