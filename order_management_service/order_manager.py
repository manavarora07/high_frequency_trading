from orders.models import Order
from order_management_service.order_execution.order_execution import execute_order

def handle_order(order_data):
    """
    Validates and handles an incoming order.
    """
    required_fields = ['symbol', 'side', 'price', 'quantity']
    if not all(k in order_data for k in required_fields):
        raise ValueError("Invalid order format")

    # Save to DB
    order = Order.objects.create(
        symbol=order_data['symbol'],
        side=order_data['side'],
        price=order_data['price'],
        quantity=order_data['quantity'],
        status="PENDING"
    )

    # Sync or async execution
    result = execute_order(order)
    return result
