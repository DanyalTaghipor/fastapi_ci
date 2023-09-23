from fastapi import APIRouter, Depends, HTTPException, Body
from sqlalchemy.orm import Session
from db.session import get_db
from models import CoinManager
from schema import Coin, CoinCreate
import services

router = APIRouter(
    tags=['Coin Manager'],
    prefix='/coin_manager'
)


@router.post("/", response_model=Coin)
def create_new_coin(coin: CoinCreate, db: Session = Depends(get_db)):
    return services.create_coin(db, coin)


@router.get("/{coin_id}/", response_model=Coin)
def get_specific_coin(coin_id: int, db: Session = Depends(get_db)):
    db_coin = services.get_coin(db, coin_id)
    if not db_coin:
        raise HTTPException(status_code=404, detail="Coin not found")
    return db_coin


@router.get("/", response_model=list[Coin])
def list_coins(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return services.get_coins(db, skip=skip, limit=limit)


@router.put("/{coin_id}/", response_model=Coin)
def update_specific_coin(coin_id: int, coin: CoinManager, db: Session = Depends(get_db)):
    return services.update_coin(db, coin_id, coin)


@router.delete("/{coin_id}/", response_model=dict)
def delete_specific_coin(coin_id: int, db: Session = Depends(get_db)):
    return services.delete_coin(db, coin_id)