from django.core.management.base import BaseCommand
from core.models import MarketData  # Now Django will load correctly

class Command(BaseCommand):
    help = "Fetch market data"

    def handle(self, *args, **kwargs):
        print("Fetching market data...")
