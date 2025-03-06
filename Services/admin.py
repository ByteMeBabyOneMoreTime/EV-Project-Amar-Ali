from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import Service, Payment

@admin.register(Service)
class Service(ModelAdmin):
    pass

@admin.register(Payment)
class Payment(ModelAdmin):
    pass
