from sqlalchemy.orm import Session
from fastapi import HTTPException
from models import CoinManager
from db.session import get_db

def get_coin(db: Session, coin_id: int):
    return db.query(CoinManager).filter(CoinManager.id == coin_id).first()

def get_coins(db: Session, skip: int = 0, limit: int = 10):
    return db.query(CoinManager).offset(skip).limit(limit).all()

def create_coin(db: Session, coin: CoinManager):
    db.add(coin)
    db.commit()
    db.refresh(coin)
    return coin

def update_coin(db: Session, coin_id: int, updated_coin: CoinManager):
    db_coin = db.query(CoinManager).filter(CoinManager.id == coin_id).first()
    if not db_coin:
        raise HTTPException(status_code=404, detail="Coin not found")
    for var, value in vars(updated_coin).items():
        setattr(db_coin, var, value)
    db.commit()
    db.refresh(db_coin)
    return db_coin

def delete_coin(db: Session, coin_id: int):
    db_coin = db.query(CoinManager).filter(CoinManager.id == coin_id).first()
    if not db_coin:
        raise HTTPException(status_code=404, detail="Coin not found")
    db.delete(db_coin)
    db.commit()
    return {"message": "Coin deleted successfully"}
