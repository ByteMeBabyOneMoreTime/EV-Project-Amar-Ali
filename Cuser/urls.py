from django.urls import path
from .views import register_customer, add_customer_details, select_service, payment_success, login, clogout

urlpatterns = [
    path("register-customer/", register_customer, name="register_customer"),
    path("customer-details/<int:user_id>/", add_customer_details, name="add_customer_details"),
    path("select-service/<int:user_id>/", select_service, name="select_service"),
    path("payment-success/<int:user_id>/", payment_success, name="payment_success"),
    path("login/", login, name="login"),
    path("logout/", clogout, name="logout")
]
