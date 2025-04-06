from binance.client import Client
import os

def get_binance_client():
    return Client(
        api_key=os.getenv("BINANCE_API_KEY"),
        api_secret=os.getenv("BINANCE_API_SECRET")
    )

def fetch_latest_trades(symbol="BTCUSDT", limit=5):
    client = get_binance_client()
    return client.get_recent_trades(symbol=symbol, limit=limit)
