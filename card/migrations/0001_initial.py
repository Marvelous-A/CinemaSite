# Generated by Django 4.2.7 on 2024-02-09 18:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cinema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('number_halls', models.IntegerField(null=True)),
                ('halls_detal', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('img_url', models.URLField()),
                ('discription', models.CharField(max_length=1000)),
                ('year', models.IntegerField(null=True)),
                ('country', models.CharField(max_length=50)),
                ('director', models.CharField(max_length=50)),
                ('duration', models.CharField(max_length=20)),
                ('cinemas_detals', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Hall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cinema_name', models.CharField(max_length=60)),
                ('time', models.CharField(max_length=10)),
                ('price', models.IntegerField(null=True)),
                ('format', models.CharField(max_length=5)),
                ('rows', models.IntegerField(null=True)),
                ('places', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brone_places', models.CharField(max_length=550)),
                ('resault_price', models.CharField(max_length=550)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=12)),
                ('birth_date', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=150)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
