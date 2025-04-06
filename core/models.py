from django.db import models

class MarketData(models.Model):
    symbol = models.CharField(max_length=10)
    price = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Order(models.Model):
    BUY = 'BUY'
    SELL = 'SELL'
    ORDER_TYPES = [(BUY, 'Buy'), (SELL, 'Sell')]

    symbol = models.CharField(max_length=10)
    order_type = models.CharField(max_length=4, choices=ORDER_TYPES)
    quantity = models.IntegerField()
    price = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.order_type} {self.quantity} {self.symbol} at {self.price}"
