from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import re
from datetime import timedelta
from django.core.exceptions import ValidationError  

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=50)
    category_discription = models.CharField(max_length=150)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.category_name}'
    
class Director(models.Model):
    name = models.CharField(max_length = 50)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'
    
class Film(models.Model):
    title = models.CharField(max_length=50)
    category = models.ManyToManyField(Category)
    img_url = models.URLField()
    discription =  models.CharField(max_length=1000)
    year = models.IntegerField(null=True)
    country = models.CharField(max_length=50)
    director = models.ManyToManyField(Director)
    duration = models.IntegerField(null=True)
    # cinemas_detals = models.CharField(max_length=1000)

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
    fk_cinema_halls	= models.ManyToManyField('Hall')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.id} {self.name}'

class Hall(models.Model):
    id = models.IntegerField(primary_key=True)
    number = models.IntegerField(null=True)
    cinema_name = models.CharField(max_length=50)
    price = models.IntegerField(null=True)
    format = models.CharField(max_length=5)
    rows = models.IntegerField(null=True)
    places = models.IntegerField(null=True)
    getting_started = models.TimeField(null=True)
    end_work = models.TimeField(null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.id} {self.cinema_name} {self.price}р {self.format}'
    
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    position = models.CharField(max_length=10)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Booking: {self.user.username}, {self.cinema}, {self.hall}, {self.film}'

class Screening(models.Model):
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def clean(self):
        # Проверка, что фильм не идет одновременно с другими фильмами в этом зале
        overlapping_screenings = Screening.objects.filter(
            hall=self.hall,
            end_time__gt=self.start_time,
            start_time__lt=self.end_time
        ).exclude(pk=self.pk)
        if overlapping_screenings.exists():
            raise ValidationError('Screening times overlap with another screening in the same hall.')

        if (self.end_time - self.start_time) > timedelta(minutes=self.film.duration + 20):
            raise ValidationError('Screening duration exceeds hall operating hours or does not allow for a 20-minute break.')
        
        

    def save(self, *args, **kwargs):
        self.full_clean()  # Вызов clean метода перед сохранением
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Фильм: {self.film.title}, кинотеатр: {self.hall.cinema_name}, начинается: {self.start_time}'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=12)
    birth_date = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    is_employer = models.BooleanField(default=False)

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
    










from mptt.models import MPTTModel, TreeForeignKey
 

class MenuItem(MPTTModel):
    name = models.CharField(max_length=255)
    parent = TreeForeignKey('self', 
                            on_delete=models.CASCADE, 
                            null=True, 
                            blank=True, 
                            related_name='children')
    url = models.CharField(max_length=255)

    def __str__(self):
        return self.name