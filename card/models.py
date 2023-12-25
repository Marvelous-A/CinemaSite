from django.db import models
from django.contrib.auth.models import AbstractUser
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

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    is_moderator = models.BooleanField()
    date_birth = models.DateField()
    city = models.CharField(max_length = 150)
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name="customuser_groups",
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="customuser_permissions",
        related_query_name="user",
    )

    def validate_phone_number(self):
        if self.phone[0] == '+' and re.fullmatch(r'[0-9]{11,15}', self.phone):
            self.phone = self.phone[0:2]+'('+self.phone[2:5]+')'+self.phone[5:8]+'-'+self.phone[8:10]+'-'+self.phone[10:]
            return True
        elif self.phone[0] != '+' and re.fullmatch(r'[0-9]{11,15}', self.phone):
            self.phone = self.phone[0:1]+'('+self.phone[1:4]+')'+self.phone[4:7]+'-'+self.phone[7:9]+'-'+self.phone[9:]
            return True
        else: return False

    def email_validate(self):
        if re.fullmatch(r'[a-zA-Z0-9.]+@[a-zA-Z0-9]+\.[a-zA-Z]+', self.email):
            print("True")
            return True
        else:
            print('False')
            return False
    
    def city_validate(self):
        if re.fullmatch(r'[А-Я][а-яА-Я-]+', self.city):
            return True
        else: 
            return False

    def save(self, *args, **kwargs):
        if self.validate_phone_number() and self.email_validate() and self.city_validate():
            super().save(*args, **kwargs)
