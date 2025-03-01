from django.urls import path
from .views import *

urlpatterns = [
    path('about/', view=about, name='about_page'),
    path("contact/", view=contact_us, name="contact_page"),
    path("services/", view=services, name="services_page"),
    path("announcements/", view=announcement, name="announcements"),
    path('', view=home, name="homepage")
]
