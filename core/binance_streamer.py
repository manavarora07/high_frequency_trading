import json
import threading
from websocket import WebSocketApp
from collections import deque

# A thread-safe store for last N trades
recent_trades = deque(maxlen=50)

def on_message(ws, message):
    data = json.loads(message)
    if 'p' in data:  # trade data
        trade = {
            'price': float(data['p']),
            'quantity': float(data['q']),
            'timestamp': data['T'],
            'symbol': data['s'],
        }
        recent_trades.append(trade)

def start_ws(symbol='btcusdt'):
    stream_url = f"wss://stream.binance.com:9443/ws/{symbol}@trade"

    def run():
        ws = WebSocketApp(stream_url, on_message=on_message)
        ws.run_forever()

    threading.Thread(target=run, daemon=True).start()
