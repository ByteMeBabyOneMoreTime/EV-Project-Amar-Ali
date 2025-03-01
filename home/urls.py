from django.urls import path

from .views import *

urlpatterns = [
    path("referral/", referral_program, name="referral"),
    path("join_program/", join_page, name="join_page"),
    
    path("announcements/", view=announcements, name="announcements"),
    path("about/", view=about, name="about_page"),
    path("contact/", view=contact_us, name="contact_page"),
    path("services/", view=services, name="services_page"),
    path("", view=home, name="homepage"),
]
