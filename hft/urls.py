from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/plot/')),  # Redirect root to /plot/
    path('core/', include('core.urls')),
    path('orders/', include('orders.urls')),
    path('plot/', include('plots.urls')),
]
