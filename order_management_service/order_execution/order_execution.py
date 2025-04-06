from orders.models import Order
from .kafka_producer import send_order_execution_report

def execute_order(order):
    """
    Simulates trade execution logic.
    """
    order.status = "FILLED"  # Simulated
    order.save()

    # Send execution report via Kafka
    send_order_execution_report({
        "order_id": order.id,
        "symbol": order.symbol,
        "status": order.status,
        "fill_price": float(order.price),
        "quantity": order.quantity,
    })

    return order
