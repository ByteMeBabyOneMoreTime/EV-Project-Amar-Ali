from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    # Other URL paths
    path('', include('home.urls')),
    path('', include('Employee_management.urls')),
    path('', include('announcement.urls')),
]