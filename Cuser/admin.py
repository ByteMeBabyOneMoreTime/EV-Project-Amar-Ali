from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import Role , Customer

@admin.register(Role)
class role(ModelAdmin):
    pass

@admin.register(Customer)
class Cuser(ModelAdmin):
    pass