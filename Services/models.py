from django.db import models
from django.contrib.auth.models import User

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
