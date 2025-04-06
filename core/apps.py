# core/apps.py

from django.apps import AppConfig
import threading

class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def ready(self):
        from .kafka_consumer import consume_trades

        def start_consumer_thread():
            thread = threading.Thread(target=consume_trades, daemon=True)
            thread.start()
            print(" Kafka consumer thread started.")

        start_consumer_thread()
