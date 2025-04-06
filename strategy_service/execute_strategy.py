import pandas as pd
from strategy_service.strategy.simple_moving_average import SimpleMovingAverage
from strategy_service.execution.order_execution import OrderExecution
from strategy_service.logs.trade_logger import log_trade

from strategy_service.logs.trade_logger import log_trade

def execute_order(symbol, quantity, order_type, price):
    # Simulate trade execution
    print(f"Executing order: {symbol}, Quantity: {quantity}, Type: {order_type}, Price: {price}")

    # Log the trade after execution
    log_trade(symbol=symbol, quantity=quantity, order_type=order_type, price=price)

# Example usage (you can remove this in production)
execute_order("BTC-USD", 1, "market", "Market Price")



# Initialize strategy and order execution system
strategy = SimpleMovingAverage(short_window=3, long_window=5)
order_execution = OrderExecution()

# Sample market data (Convert dictionary to DataFrame)
market_data = pd.DataFrame({
    "close": [65000, 65200, 64800, 65150, 65300, 65400, 65500, 65600, 65750, 65800, 66000, 66200]
})

# Generate trading signals
signals = strategy.generate_signals(market_data)

for index, row in signals.iterrows():
    if row["signal"] == 1:  # Buy Signal
        order = {
            "symbol": "BTC-USD",
            "quantity": 1,
            "order_type": "market",
            "price": "Market Price"
        }
        order_execution.execute_order(order)

