# Generated by Django 4.2.7 on 2023-11-12 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0006_cinema'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='img_url',
            field=models.URLField(),
        ),
    ]
