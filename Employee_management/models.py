from django.db import models

class Employee(models.Model):
    Full_Name = models.CharField(verbose_name="Full name",max_length=200, help_text="Name of the employee")
    Date_of_birth = models.DateField(verbose_name="Date of Birth")
    
    GENDER = {
        ("Male" , "Male"),
        ("Female" , "Female"),
        ("Other" , "Other")
    }
    Gender = models.CharField(verbose_name="Gender",max_length=40, choices=GENDER)
    Father_Name = models.CharField(verbose_name="Fathers Name",max_length=200)
    
    MSTATUS = {
        ('Married', 'Married'),
        ('Un Married', 'Un Married')
    }
    Marital_Status = models.CharField(default="Un Married",verbose_name="Maritial Status", blank=True, null=True, max_length=40, choices=MSTATUS)
    
    Current_Address = models.TextField(verbose_name="Current Address")
    Permanent_Address = models.TextField(verbose_name="Permanent Address")
    Contact_Number = models.CharField(max_length=30, verbose_name="Contact Details")
    Email_id = models.EmailField(max_length=254)
    
    Addhar_number = models.CharField(max_length=15)
    Pan_number = models.CharField(max_length=15)
    
    Emergency_Contact_Number = models.CharField(max_length=30)
    
    Job_role = models.TextField(default='', blank=True)
    
    Created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.Full_Name
    
class Salary(models.Model):
    Designatory = models.ForeignKey(Employee, verbose_name="Employee", on_delete=models.PROTECT)
    
    Gross_Salary = models.CharField(verbose_name="Gross Salary (Total Earnings)", max_length=50)
    Total_decuctions = models.CharField(verbose_name="Total Deductions", max_length=50)
    Net_Salary = models.CharField(verbose_name="Net Salary (Take-Home Pay)", max_length=50)

    Created_at = models.DateTimeField(auto_now=True)
    
class Payslip(models.Model):
    Designatory = models.ForeignKey(Employee, on_delete=models.PROTECT)
    
    Payment_method = models.CharField(max_length=500)
    Payment_date = models.DateField()
    