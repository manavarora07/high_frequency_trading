from confluent_kafka import Consumer, KafkaError
from django.core.management.base import BaseCommand
from django.conf import settings

class Command(BaseCommand):
    help = 'Consume trade data from Kafka topic'

    def handle(self, *args, **kwargs):
        conf = {
            'bootstrap.servers': settings.KAFKA_CONFIG['BOOTSTRAP_SERVERS'],
            'group.id': 'hft_group',
            'auto.offset.reset': 'earliest',
        }
        consumer = Consumer(conf)
        consumer.subscribe([settings.KAFKA_CONFIG['TOPIC_NAME']])

        self.stdout.write("Started consuming trade data from Kafka...")

        try:
            while True:
                msg = consumer.poll(1.0)
                if msg is None:
                    continue
                if msg.error():
                    if msg.error().code() != KafkaError._PARTITION_EOF:
                        print("Consumer error: {}".format(msg.error()))
                    continue
                print(f"Received: {msg.value().decode('utf-8')}")
        except KeyboardInterrupt:
            pass
        finally:
            consumer.close()
