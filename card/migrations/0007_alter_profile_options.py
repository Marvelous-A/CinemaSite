# Generated by Django 4.2.7 on 2024-03-18 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0006_remove_film_cinemas_detals'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'permissions': [('employer', 'Сотрудник')]},
        ),
    ]
