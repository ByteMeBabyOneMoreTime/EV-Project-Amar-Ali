from django.urls import path

from .views import *

urlpatterns = [
    path("join/", view=join, name="join_page"),
    path("referral/", view=referral, name="referral_page"),
    path("announcements/", view=announcements, name="announcements_page"),
    path("about/", view=about, name="about_page"),
    path("contact/", view=contact_us, name="contact_page"),
    path("services/", view=services, name="services_page"),
    path("", view=home, name="homepage"),
]
