# Generated by Django 4.2.7 on 2024-03-08 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0018_remove_hall_fk_halls_cinema_delete_halls_films'),
    ]

    operations = [
        migrations.AddField(
            model_name='hall',
            name='cinema_name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]