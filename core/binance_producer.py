import json
import time
import sys
from kafka import KafkaProducer
from .binance_service import fetch_latest_trades  

# Kafka setup
def create_producer():
    while True:
        try:
            producer = KafkaProducer(
                bootstrap_servers='localhost:9092',
                value_serializer=lambda v: json.dumps(v).encode('utf-8')
            )
            print("✅ Kafka producer connected.")
            return producer
        except Exception as e:
            print(f"⚠️ Kafka broker not available: {e}. Retrying in 3 seconds...")
            time.sleep(3)

producer = create_producer()

# Produce loop
def produce_binance_trades():
    while True:
        try:
            trades = fetch_latest_trades("BTCUSDT", limit=5)
            for trade in trades:
                producer.send("trades", value=trade)
                print(f"📤 Sent trade: {trade}")
        except Exception as e:
            print(f"❌ Error producing trades: {e}", file=sys.stderr)
        time.sleep(5)
