from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Employee, Salary, Payslip

@admin.register(Employee)
class Employee(ModelAdmin):
    pass

@admin.register(Salary)
class Salary(ModelAdmin):
    pass

@admin.register(Payslip)
class Payslip(ModelAdmin):
    pass