from django.db import models
from django.contrib.auth.models import AbstractUser

class Film(models.Model):
    title = models.CharField(max_length=50)
    img_url = models.CharField(max_length=800)
    discription =  models.CharField(max_length=1000)
    year = models.IntegerField(null=True)
    country = models.CharField(max_length = 50)
    director = models.CharField(max_length = 50)
    duration = models.CharField(max_length = 20)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Tel: {self.title}'
    
class MyUser(AbstractUser):
    age = models.PositiveIntegerField(blank = True)
