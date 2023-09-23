from pydantic import BaseModel

class CoinBase(BaseModel):
    name: str
    symbol: str
    price: float

class CoinCreate(CoinBase):
    pass

class Coin(CoinBase):
    id: int

    class Config:
        orm_mode = True