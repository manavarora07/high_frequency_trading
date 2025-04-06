from abc import ABC, abstractmethod

class BaseStrategy(ABC):
    def __init__(self, market_data, order_manager):
        self.market_data = market_data
        self.order_manager = order_manager

    @abstractmethod
    def generate_signal(self):
        """Generate buy/sell signals based on market data"""
        pass

    def execute_trade(self, signal, quantity=1):
        """Executes trade based on signal"""
        if signal == "BUY":
            self.order_manager.place_order("BUY", quantity)
        elif signal == "SELL":
            self.order_manager.place_order("SELL", quantity)
