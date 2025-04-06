import csv
import random
import time
from datetime import datetime, timezone

TRADE_FILE = "trade_log.csv"
SYMBOLS = ["BTC-USD", "ETH-USD", "LTC-USD", "XRP-USD", "DOGE-USD"]
ORDER_TYPES = ["market", "limit"]
STATUS = "executed"

def generate_fake_trade():
    return {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "symbol": random.choice(SYMBOLS),
        "quantity": random.randint(1, 10),
        "order_type": random.choice(ORDER_TYPES),
        "price": "Market Price",
        "status": STATUS,
    }

def append_trade_to_csv(trade):
    file_exists = False
    try:
        with open(TRADE_FILE, "r", newline="") as f:
            file_exists = True
    except FileNotFoundError:
        pass

    with open(TRADE_FILE, "a", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=trade.keys())
        if not file_exists:
            writer.writeheader()
        writer.writerow(trade)

if __name__ == "__main__":
    print("Simulating trades... Press Ctrl+C to stop.\n")
    try:
        while True:
            trade = generate_fake_trade()
            append_trade_to_csv(trade)
            print(f"Trade logged: {trade}")
            time.sleep(random.uniform(0.2, 1.0))  # simulate trades every 200ms–1s
    except KeyboardInterrupt:
        print("\nStopped trade simulation.")
