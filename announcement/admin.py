from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import information

@admin.register(information)
class information(ModelAdmin):
    class Meta:
        verbose_name = 'Website Announcements'
        verbose_name_plural = 'Announcements'
