# Generated by Django 5.1.6 on 2025-03-01 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('announcement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Heading', models.CharField(max_length=500, verbose_name='Headline')),
                ('Text', models.TextField(verbose_name='Announcement')),
                ('created_at', models.DateField(auto_now=True, verbose_name='Date Created')),
            ],
        ),
    ]
