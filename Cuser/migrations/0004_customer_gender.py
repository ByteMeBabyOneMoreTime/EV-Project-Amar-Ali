# Generated by Django 5.1.6 on 2025-03-02 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cuser', '0003_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='Male', max_length=200),
        ),
    ]
