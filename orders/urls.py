from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='order_index'),  # You can define more views later
]
