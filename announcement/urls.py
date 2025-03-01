from django.urls import path
from .views import get_anouncements
urlpatterns = [
    path("announcement", get_anouncements, name="announcement"),
]
