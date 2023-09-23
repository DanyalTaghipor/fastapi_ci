import pytest
from api.coin_manager.services import get_coin, get_coins, create_coin, update_coin, delete_coin

def test_create_coin(test_app, test_db):
    response = test_app.post("/coin/", json={"name": "Bitcoin", "symbol": "BTC", "price": 45000.0})
    assert response.status_code == 200
    assert response.json()["name"] == "Bitcoin"
    assert response.json()["symbol"] == "BTC"
    assert response.json()["price"] == 45000.0


def test_get_coin(test_app, test_db):
    response = test_app.post("/coin/", json={"name": "Ethereum", "symbol": "ETH", "price": 3000.0})
    coin_id = response.json()["id"]
    
    response = test_app.get(f"/coin/{coin_id}/")
    assert response.status_code == 200
    assert response.json()["name"] == "Ethereum"


def test_get_coins(test_app, test_db):
    response = test_app.get("/coins/?skip=0&limit=10")
    assert response.status_code == 200
    assert len(response.json()) == 2


def test_update_coin(test_app, test_db):
    response = test_app.post("/coin/", json={"name": "Ripple", "symbol": "XRP", "price": 1.0})
    coin_id = response.json()["id"]
    
    response = test_app.put(f"/coin/{coin_id}/", json={"name": "Ripple", "symbol": "XRP", "price": 1.5})
    assert response.status_code == 200
    assert response.json()["price"] == 1.5
    assert response.json()["name"] == "Ripple"


def test_delete_coin(test_app, test_db):
    response = test_app.post("/coin/", json={"name": "Litecoin", "symbol": "LTC", "price": 200.0})
    coin_id = response.json()["id"]
    
    response = test_app.delete(f"/coin/{coin_id}/")
    assert response.status_code == 200
    assert response.json()["message"] == "Coin deleted successfully"
    
    response = test_app.get(f"/coin/{coin_id}/")
    assert response.status_code == 404