from django.db import models

class Order(models.Model):
    ORDER_STATUS = (
        ('PENDING', 'Pending'),
        ('FILLED', 'Filled'),
        ('CANCELLED', 'Cancelled'),
        ('REJECTED', 'Rejected'),
    )

    symbol = models.CharField(max_length=10)
    side = models.CharField(max_length=4)  # BUY / SELL
    price = models.DecimalField(max_digits=12, decimal_places=2)
    quantity = models.IntegerField()
    status = models.CharField(max_length=10, choices=ORDER_STATUS, default='PENDING')
    timestamp = models.DateTimeField(auto_now_add=True)
