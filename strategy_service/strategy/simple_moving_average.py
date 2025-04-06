import pandas as pd
import numpy as np
from market_data_service.market_data import MarketData

class SimpleMovingAverage:
    def __init__(self, short_window=3, long_window=5):
        self.short_window = short_window
        self.long_window = long_window

    def generate_signals(self, data):
        print("🔍 Checking Data Before Processing:")
        print(data.head())  # Print first few rows

        if "close" not in data.columns:
            raise ValueError("❌ 'close' column is missing from data!")

        data["short_ma"] = data["close"].rolling(window=self.short_window).mean()
        data["long_ma"] = data["close"].rolling(window=self.long_window).mean()
        data["signal"] = (data["short_ma"] > data["long_ma"]).astype(int)
        
        return data  # ✅ This line is inside the function!

# ✅ Ensure you're creating an instance of the class before calling `generate_signals()`
if __name__ == "__main__":
    historical_data = pd.DataFrame({"close": [65000, 65200, 64800, 65150, 65300, 65400, 65500, 65600, 65750, 65800, 66000, 66200]})
    
    strategy = SimpleMovingAverage(short_window=3, long_window=5)
    signals = strategy.generate_signals(historical_data)

    print("📈 Generated Trading Signals:")
    print(signals)
