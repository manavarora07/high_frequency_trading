from celery import shared_task
from order_management_service.order_manager import handle_order

@shared_task
def process_kafka_order(order_data):
    """
    Handles order from Kafka in background using Celery.
    """
    try:
        return handle_order(order_data)
    except Exception as e:
        print("Error processing order:", e)
