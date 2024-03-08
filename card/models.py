from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import re

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=50)
    category_discription = models.CharField(max_length=150)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.category_name}'
    
class Director(models.Model):
    director_name = models.CharField(max_length = 50)
    director_id = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.director_name}'
    
class Film(models.Model):
    title = models.CharField(max_length=50)
    category = models.ManyToManyField(Category)
    img_url = models.URLField()
    discription =  models.CharField(max_length=1000)
    year = models.IntegerField(null=True)
    country = models.CharField(max_length=50)
    director = models.ManyToManyField(Director)
    duration = models.CharField(max_length=20)
    cinemas_detals = models.CharField(max_length=1000)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Film: {self.title}'

class Cinema(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=60)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    number_halls = models.IntegerField(null=True)
    # fk_cinema_halls	= models.ForeignKey('Hall', on_delete=models.PROTECT, null=True)
    # fk_cinema_halls	= models.ManyToManyField('Hall')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.id} {self.name}'

class Hall(models.Model):
    id = models.IntegerField(primary_key=True)
    # cinema_name = models.CharField(max_length=60)
    # time = models.CharField(max_length=10)
    price = models.IntegerField(null=True)
    format = models.CharField(max_length=5)
    rows = models.IntegerField(null=True)
    places = models.IntegerField(null=True)
    fk_halls_cinema	= models.ForeignKey('Cinema', on_delete=models.PROTECT, null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.id} |{self.fk_halls_cinema}| {self.price}р {self.format}'

class Halls_Films(models.Model):
    id = models.IntegerField(primary_key=True)
    hall_id = models.IntegerField(null=True)
    film_id = models.IntegerField(null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return f'id: {self.id} | id Hall: {self.hall_id} | id Film: {self.film_id}'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=12)
    birth_date = models.CharField(max_length=150)
    city = models.CharField(max_length=150)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Profile: {self.user.username}'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kawrgs):
    instance.profile.save()


class Payment(models.Model):
    brone_places = models.CharField(max_length=550)
    resault_price = models.CharField(max_length=550)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return f'resault price: {self.resault_price}'