# Generated by Django 5.1.6 on 2025-03-02 20:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cuser', '0002_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('generated_id', models.CharField(editable=False, max_length=8, unique=True)),
                ('father_name', models.CharField(max_length=400)),
                ('phone_number', models.CharField(max_length=12)),
                ('aadhar_number', models.CharField(max_length=12)),
                ('address', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Employee', to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Customer', to=settings.AUTH_USER_MODEL, verbose_name='Customer')),
            ],
        ),
    ]
