from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import Service, Payment, Perks

@admin.register(Service)
class Service(ModelAdmin):
    pass

@admin.register(Payment)
class Payment(ModelAdmin):
    pass

@admin.register(Perks)
class Payment(ModelAdmin):
    pass
