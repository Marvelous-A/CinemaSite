# Generated by Django 4.2.7 on 2024-03-17 21:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0005_hall_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='film',
            name='cinemas_detals',
        ),
    ]