# Generated by Django 4.2.7 on 2024-03-08 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0012_remove_cinema_halls_detal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hall',
            name='time',
        ),
    ]
