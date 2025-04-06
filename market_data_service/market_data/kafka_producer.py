from kafka import KafkaProducer
import json

KAFKA_BROKER = 'kafka:9092'
TOPIC = 'market_data'

producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def send_market_data(ticker, price):
    """ Sends market data (ticker price update) to Kafka """
    data = {'ticker': ticker, 'price': price}
    producer.send(TOPIC, value=data)
    producer.flush()
    print(f"Sent market data: {data}")

if __name__ == "__main__":
    send_market_data("AAPL", 175.30)  # Example stock data
