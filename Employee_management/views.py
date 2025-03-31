from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

from django.core.exceptions import PermissionDenied
from Cuser.models import Role
from django.db import models
from .forms import EmployeeCreationForm

User = get_user_model()


@login_required
def create_employee(request):
    if not request.user.is_superuser:
        raise PermissionDenied("Only superusers can create employee accounts.")

    form = EmployeeCreationForm(request.POST or None)
    success = False
    error = None

    if request.method == 'POST':
        if form.is_valid():
            try:
                user = form.save(commit=False)
                user.is_staff = True
                user.save()

                Role.objects.create(user=user, role='Employee')
                success = True
                form = EmployeeCreationForm()  # Reset form on success
            except Exception as e:
                error = f"Error creating employee: {str(e)}"

    context = {
        'form': form,
        'success': success,
        'error': error
    }

    if request.headers.get('HX-Request'):
        return render(request, 'dashboard/create_employee.html', context)

    return render(request, 'dashboard/create_employee.html', context)


@login_required
def employee_list(request):
    if not request.user.is_superuser:
        raise PermissionDenied("Only superusers can view employee list.")

    # Get employees and annotate each with their customer count
    employees = (Role.objects
                 .filter(role='Employee')
                 .select_related('user')
                 .annotate(customer_count=models.Count('user__Employee'))
                 )

    context = {
        'employees': employees,
    }
    return render(request, 'dashboard/employee_list.html', context)
