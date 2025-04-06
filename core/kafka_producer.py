from confluent_kafka import Producer
from django.conf import settings

conf = {'bootstrap.servers': settings.KAFKA_CONFIG['BOOTSTRAP_SERVERS']}
producer = Producer(conf)

def delivery_report(err, msg):
    if err is not None:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to {msg.topic()} [{msg.partition()}]')

def produce_trade_data(data):
    producer.produce(
        settings.KAFKA_CONFIG['TOPIC_NAME'],
        key=str(data.get("trade_id", "0")),
        value=str(data),
        callback=delivery_report
    )
    producer.flush()
