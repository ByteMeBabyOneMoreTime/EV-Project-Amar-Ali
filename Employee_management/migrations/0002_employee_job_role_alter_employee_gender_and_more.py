# Generated by Django 5.1.6 on 2025-02-15 14:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee_management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='Job_role',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='employee',
            name='Gender',
            field=models.CharField(choices=[('Female', 'Female'), ('Other', 'Other'), ('Male', 'Male')], max_length=40),
        ),
        migrations.AlterField(
            model_name='employee',
            name='Marital_Status',
            field=models.CharField(blank=True, choices=[('Married', 'Married'), ('Un Married', 'Un Married')], default='Un Married', max_length=40, null=True),
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Gross_Salary', models.CharField(max_length=50, verbose_name='Gross Salary (Total Earnings)')),
                ('Total_decuctions', models.CharField(max_length=50, verbose_name='Total Deductions')),
                ('Designatory', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Employee_management.employee', verbose_name='Employee')),
            ],
        ),
    ]
