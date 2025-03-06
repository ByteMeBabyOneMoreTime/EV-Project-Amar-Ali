from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
import random
from django.core.exceptions import ValidationError

class Role(models.Model):
    user = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.CASCADE)

    ROLE_CHOICES = [  
        ('Customer', 'Customer'),
        ('Employee', 'Employee')
    ]
    
    role = models.CharField(choices=ROLE_CHOICES, max_length=200)

    def __str__(self):
        return f"{self.user.username} - {self.role}"  

class Customer(models.Model):
    user = models.ForeignKey(User, verbose_name=_("Customer"), related_name='Customer', on_delete=models.CASCADE)
    
    generated_id = models.CharField(max_length=8, unique=True, editable=False)
    GENDER = [
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other")
    ]
    gender = models.CharField(choices=GENDER, max_length=200, default="Male")
    father_name = models.CharField(max_length=400)
    phone_number = models.CharField(max_length=12)
    aadhar_number = models.CharField(max_length=12)
    address = models.TextField()
    
    created_by = models.ForeignKey(User, verbose_name=_("Created By"), related_name='Employee', on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    
    def clean(self):
        # Check if user has role 'Customer'
        user_role = Role.objects.filter(user=self.user, role="Customer").exists()
        if not user_role:
            raise ValidationError({"user": "Selected user must have the role of Customer."})

        # Check if created_by has role 'Employee'
        creator_role = Role.objects.filter(user=self.created_by, role="Employee").exists()
        if not creator_role:
            raise ValidationError({"created_by": "Creator must have the role of Employee."})

    def save(self, *args, **kwargs):
        self.clean()  # Validate before saving
        if not self.generated_id:  # Generate only if it's not already assigned
            self.generated_id = self.generate_unique_id()
        super().save(*args, **kwargs)

    @staticmethod
    def generate_unique_id():
        while True:
            new_id = str(random.randint(10000000, 99999999))  # Generate an 8-digit number
            if not Customer.objects.filter(user_id=new_id).exists():
                return new_id

