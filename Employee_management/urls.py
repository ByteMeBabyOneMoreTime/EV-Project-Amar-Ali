from django.urls import path
from .views import create_employee, employee_list

urlpatterns = [
    path('create/', create_employee, name='create_employee'),
    path('list/', employee_list, name='employee_list'),
]
