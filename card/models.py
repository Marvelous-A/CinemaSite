from django.db import models
#from django.utils.translation import gettext_lazy as _
import re

class Film(models.Model):
    title = models.CharField(max_length=50)
    img_url = models.URLField()
    discription =  models.CharField(max_length=1000)
    year = models.IntegerField(null=True)
    country = models.CharField(max_length=50)
    director = models.CharField(max_length=50)
    duration = models.CharField(max_length=20)
    cinemas_detals = models.CharField(max_length=1000)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Tel: {self.title}'

class Cinema(models.Model):
    name = models.CharField(max_length=60)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    number_halls = models.IntegerField(null=True)
    halls_detal = models.CharField(max_length=1000)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Tel: {self.name}'

class Hall(models.Model):
    cinema_name = models.CharField(max_length=60)
    time = models.CharField(max_length=10)
    price = models.IntegerField(null=True)
    format = models.CharField(max_length=5)
    rows = models.IntegerField(null=True)
    places = models.IntegerField(null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Tel: {self.cinema_name} {self.time} {self.price}р {self.format}'

class Profile(models.Model):
    phone_number = models.CharField(max_length=12)
    email = models.CharField(max_length=150)
    birth_date = models.CharField(max_length=150)
    city = models.CharField(max_length=150)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return f'email: {self.email}'
    
class Payment(models.Model):
    brone_places = models.CharField(max_length=550)
    resault_price = models.CharField(max_length=550)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return f'resault price: {self.resault_price}'