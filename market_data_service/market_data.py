import pandas as pd

class MarketData:
    def fetch_data(self, symbol, start, end):
        # Example: Fetch historical data (replace with actual logic)
        return {
            "symbol": symbol,
            "start_date": start,
            "end_date": end,
            "prices": [65000, 65200, 64800, 65150],  # Dummy data
        }

