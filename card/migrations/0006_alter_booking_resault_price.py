# Generated by Django 4.2.7 on 2024-04-05 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0005_booking_resault_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='resault_price',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
    ]
