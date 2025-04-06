import csv
import os
from datetime import datetime

class OrderExecution:
    def __init__(self, log_file="executed_trades.csv"):
        self.log_file = log_file
        self._initialize_log()

    def _initialize_log(self):
        """Create the log file with headers if it doesn't exist."""
        if not os.path.exists(self.log_file):
            with open(self.log_file, mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["timestamp", "symbol", "quantity", "order_type", "price", "status"])

    def execute_order(self, order):
        """Execute an order and log it."""
        order["timestamp"] = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        order["status"] = "executed"

        # Simulating execution (Replace with actual API call for live trading)
        print(f"📤 Executing Order: {order}")

        # Log the order
        self._log_order(order)

    def _log_order(self, order):
        """Append the executed order to the CSV log."""
        with open(self.log_file, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([order["timestamp"], order["symbol"], order["quantity"],
                             order["order_type"], order["price"], order["status"]])
