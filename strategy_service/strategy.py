import redis
import requests  # To send orders to OMS

# Connect to Redis
redis_client = redis.Redis(host='localhost', port=6379, db=0)

# Fetch market data
price = float(redis_client.get("BTC-USD").decode("utf-8"))
print(f"Latest BTC-USD price: {price}")

# Order API endpoint (Replace with your actual order service URL)
ORDER_SERVICE_URL = "http://localhost:5000/place_order"

# Simple trading logic (buy if price < 64000, sell if price > 66000)
order = None
if price < 64000:
    order = {"symbol": "BTC-USD", "side": "buy", "quantity": 1, "price": price}
    print("Buying BTC!")
elif price > 66000:
    order = {"symbol": "BTC-USD", "side": "sell", "quantity": 1, "price": price}
    print("Selling BTC!")

# Send order to Order Management System (OMS)
if order:
    response = requests.post(ORDER_SERVICE_URL, json=order)
    if response.status_code == 200:
        print("✅ Order successfully placed!")
    else:
        print("❌ Order failed:", response.text)
else:
    print("No trade executed.")
