from django.db import models
from django.contrib.auth.models import User
from datetime import date, timedelta

class Service(models.Model):  
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)  

    def __str__(self):
        return self.name

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    service = models.ForeignKey(Service, on_delete=models.CASCADE) 
    date = models.DateField(auto_now_add=True)  
    METHOD = {
        ('Online', 'Online'),
        ('Offline', 'Offline')
    }
    method = models.CharField(choices=METHOD, max_length=20)
    online_payment_id = models.CharField(null=True, blank= True)

    def __str__(self):
        return f"Payment by {self.user.username} for {self.service.name} on {self.date}"
    
    def is_defaulter(self):
        """
        Returns True if the payment date is more than 30 days ago.
        """
        return (date.today() - self.date) > timedelta(days=30)

    def is_going_to_default(self):
        """
        Returns True if the payment date is more than 20 days ago.
        """
        return (date.today() - self.date) > timedelta(days=20)

class Perks(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    terms = models.TextField()