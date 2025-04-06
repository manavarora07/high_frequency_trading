import redis
from kafka import KafkaConsumer
import json

# Connect to Redis
redis_client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

# Connect to Kafka
consumer = KafkaConsumer(
    'market_data', 
    bootstrap_servers='kafka:9092',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("Listening for messages on market_data...")

for message in consumer:
    data = message.value
    symbol = data.get("symbol")
    price = data.get("price")

    if symbol and price:
        redis_client.set(symbol, price)
        print(f"Stored in Redis: {symbol} - {price}")
