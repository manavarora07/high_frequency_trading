from kafka import KafkaConsumer

TOPIC_NAME = "market_data"
BOOTSTRAP_SERVERS = ["kafka:9092"]

# Create Kafka consumer
consumer = KafkaConsumer(
    TOPIC_NAME,
    bootstrap_servers=BOOTSTRAP_SERVERS,
    auto_offset_reset="earliest",
    group_id="strategy_group"
)

print(f"Listening to Kafka topic: {TOPIC_NAME}")

for message in consumer:
    print(f"Received message: {message.value.decode('utf-8')}")
