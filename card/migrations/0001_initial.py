# Generated by Django 4.2.7 on 2024-01-03 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=12)),
                ('email', models.CharField(max_length=150)),
                ('birth_date', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=150)),
            ],
        ),
    ]
