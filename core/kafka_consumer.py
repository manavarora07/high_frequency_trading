from kafka import KafkaConsumer
from kafka.errors import NoBrokersAvailable
import time

def consume_trades():
    while True:
        try:
            consumer = KafkaConsumer(
                'trades',
                bootstrap_servers=['kafka:9092'],  # Docker internal hostname
                group_id='trade-group',
                auto_offset_reset='latest',
                value_deserializer=lambda m: m.decode('utf-8')
            )
            print("✅ Kafka consumer connected.")
            break
        except NoBrokersAvailable:
            print("⚠️ Kafka broker not available. Retrying in 3 seconds...")
            time.sleep(3)

    for message in consumer:
        print(f"📥 Received trade: {message.value}")
