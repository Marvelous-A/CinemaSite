# Generated by Django 4.2.7 on 2024-03-07 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0009_cinema_fk_cinema_halls_alter_cinema_id_alter_hall_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cinema',
            name='fk_cinema_halls',
        ),
        migrations.AddField(
            model_name='cinema',
            name='fk_cinema_halls',
            field=models.ManyToManyField(to='card.hall'),
        ),
    ]
