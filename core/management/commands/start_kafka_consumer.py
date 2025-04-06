from django.core.management.base import BaseCommand
from kafka import KafkaConsumer
from django.conf import settings
import time

class Command(BaseCommand):
    help = 'Start Kafka consumer to read trade messages'

    def handle(self, *args, **kwargs):
        print("📡 Starting Kafka consumer...")

        while True:
            try:
                consumer = KafkaConsumer('trades', **settings.KAFKA_CONFIG)
                print("✅ Kafka consumer connected.")
                break
            except Exception as e:
                print(f"❌ Kafka connection failed: {e}. Retrying in 3s...")
                time.sleep(3)

        for message in consumer:
            trade = message.value
            print(f"📥 Received trade: {trade}")
