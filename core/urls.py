from django.urls import path
from core.views import publish_trade
from . import views

urlpatterns = [
    path('', views.plot, name='plot'),
    path('plot-data/', views.trade_plot_data, name='plot-data'),
    path('publish/', publish_trade, name='publish_trade'),
]
