from django.shortcuts import render
from django.http import JsonResponse
from .kafka_consumer import consume_trades


def index(request):
    return render(request, 'core/index.html')

def stats(request):
    return render(request, 'core/stats.html')

def plot(request):
    return render(request, 'core/plot.html')



def trade_plot_data(request):
    return JsonResponse(consume_trades, safe=False)
