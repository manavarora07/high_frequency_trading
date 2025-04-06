from django.urls import path
from . import views

urlpatterns = [
    path('', views.plot, name='plot'),
    path('plot-data/', views.trade_plot_data, name='plot-data'),
]
