# Generated by Django 5.1.6 on 2025-03-02 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee_management', '0003_alter_employee_gender_alter_employee_marital_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='Gender',
            field=models.CharField(choices=[('Female', 'Female'), ('Other', 'Other'), ('Male', 'Male')], max_length=40, verbose_name='Gender'),
        ),
    ]
