# trade_logger.py
import csv
import random
import time
from datetime import datetime, timezone

CSV_FILE = "trade_log.csv"
SYMBOLS = ["BTC-USD", "ETH-USD", "XRP-USD", "LTC-USD"]

def generate_trade():
    return {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "symbol": random.choice(SYMBOLS),
        "quantity": random.randint(1, 10),
        "order_type": "market",
        "price": "Market Price",
        "status": "executed"
    }

def log_trade(trade):
    with open(CSV_FILE, mode="a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=trade.keys())
        if f.tell() == 0:
            writer.writeheader()
        writer.writerow(trade)
    print(f"Trade logged: {trade}")

if __name__ == "__main__":
    print("[✓] Trade logger started...")
    while True:
        trade = generate_trade()
        log_trade(trade)
        time.sleep(0.5)  # One trade every 0.5s (adjust as needed)
