import sys
import os

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from market_data_service.celery import app

@app.task
def process_market_data(data):
    print(f"Processing market data: {data}")
    return {"status": "processed", "data": data}
