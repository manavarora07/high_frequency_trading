from django.urls import path
from . import views

urlpatterns = [
    path('', views.plot_dashboard, name='plot-dashboard'),
]
