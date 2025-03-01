from django.db import models

# Create your models here.
class information(models.Model):
    Heading = models.CharField(verbose_name="Headline", max_length=500)
    Text = models.TextField(verbose_name="Announcement")
    created_at = models.DateField(verbose_name="Date Created", auto_now=True)
    
    def __str__(self):
        return f"Date: {self.created_at} Text: {self.Text}"