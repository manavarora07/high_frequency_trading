# order_management_service/order_execution/kafka_producer.py
import time
from kafka import KafkaProducer
from kafka.errors import NoBrokersAvailable

def create_kafka_producer(bootstrap_servers='kafka:9092', retries=10, delay=3):
    for i in range(retries):
        try:
            return KafkaProducer(
                bootstrap_servers=bootstrap_servers,
                value_serializer=lambda v: v.encode('utf-8')
            )
        except NoBrokersAvailable:
            print(f"[Kafka] No brokers available, retrying in {delay}s...")
            time.sleep(delay)
    raise NoBrokersAvailable("Kafka broker not available after retries")

producer = create_kafka_producer()
