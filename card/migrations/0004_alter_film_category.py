# Generated by Django 4.2.7 on 2024-02-17 22:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0003_film_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='card.category'),
        ),
    ]