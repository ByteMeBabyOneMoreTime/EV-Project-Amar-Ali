from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    # Other URL paths
    path('', include('home.urls')),
    path('employee/', include('Employee_management.urls')),
    path('', include('announcement.urls')),
    path('customer/', include('Cuser.urls')),
    path('Services/', include('Services.urls'))
]

# TODO Create the option to add employee in admin panel
