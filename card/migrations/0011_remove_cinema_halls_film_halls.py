# Generated by Django 4.2.7 on 2023-11-14 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0010_alter_cinema_halls'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cinema',
            name='halls',
        ),
        migrations.AddField(
            model_name='film',
            name='halls',
            field=models.CharField(default='fkdofko', max_length=1000),
        ),
    ]
