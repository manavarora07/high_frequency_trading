import redis

# Connect to Redis
redis_client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

# Store market data
redis_client.set("BTC-USD", 65000)

# Retrieve and print market data
price = redis_client.get("BTC-USD")
print(f"BTC-USD Price: {price}")
