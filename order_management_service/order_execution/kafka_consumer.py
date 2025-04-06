from kafka import KafkaConsumer
import json
from orders.tasks import process_kafka_order

consumer = KafkaConsumer(
    'new_orders',
    bootstrap_servers='kafka:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    auto_offset_reset='latest',
    group_id='order_manager'
)

for message in consumer:
    order_data = message.value
    process_kafka_order.delay(order_data)  # Celery task
