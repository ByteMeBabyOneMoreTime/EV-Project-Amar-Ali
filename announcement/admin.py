from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import information

@admin.register(information)
class information(ModelAdmin):
    pass
