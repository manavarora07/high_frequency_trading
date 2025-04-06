# plot/views.py
from django.shortcuts import render

def plot_dashboard(request):
    return render(request, 'plots/dashboard.html')
