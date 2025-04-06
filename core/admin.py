from django.contrib import admin
from .models import MarketData, Order
from . import binance_streamer

binance_streamer.start_ws('btcusdt')
admin.site.register(MarketData)
admin.site.register(Order)
