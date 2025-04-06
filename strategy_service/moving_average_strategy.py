import pandas as pd
from .base_strategy import BaseStrategy

class MovingAverageStrategy(BaseStrategy):
    def __init__(self, market_data, order_manager, short_window=5, long_window=20):
        super().__init__(market_data, order_manager)
        self.short_window = short_window
        self.long_window = long_window

    def generate_signal(self):
        """Computes moving averages and generates buy/sell signals"""
        df = self.market_data.get_latest_data()

        if len(df) < self.long_window:
            return None  # Not enough data to make a decision

        df['short_ma'] = df['price'].rolling(window=self.short_window).mean()
        df['long_ma'] = df['price'].rolling(window=self.long_window).mean()

        if df['short_ma'].iloc[-1] > df['long_ma'].iloc[-1] and df['short_ma'].iloc[-2] <= df['long_ma'].iloc[-2]:
            return "BUY"
        elif df['short_ma'].iloc[-1] < df['long_ma'].iloc[-1] and df['short_ma'].iloc[-2] >= df['long_ma'].iloc[-2]:
            return "SELL"

        return None
