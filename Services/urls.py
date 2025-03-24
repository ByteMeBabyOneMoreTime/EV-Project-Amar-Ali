from django.urls import path
from .views import load_services

urlpatterns = [
    path('get_services/', load_services, name='get_services'),
    # other URLs...
]