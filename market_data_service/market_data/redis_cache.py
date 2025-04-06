import redis
import json

class RedisCache:
    def __init__(self, host="localhost", port=6379, db=0):
        self.client = redis.Redis(host=host, port=port, db=db, decode_responses=True)

    def set_data(self, key, value, expiry=5):  # Cache expiry in seconds
        self.client.setex(key, expiry, json.dumps(value))

    def get_data(self, key):
        data = self.client.get(key)
        return json.loads(data) if data else None

# Example usage
if __name__ == "__main__":
    cache = RedisCache()
    cache.set_data("BTC-USD", {"price": 45000, "timestamp": "2025-04-02T12:00:00Z"})
    print(cache.get_data("BTC-USD"))
