from django import forms
from .models import Film, Cinema, Hall
# from django.contrib.auth.forms import UserCreationForm
# from .models import MyUser

class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ['title', 'img_url','discription', 'year', 'country', 'director', 'duration', 'cinemas_detals']

class CinemaForm(forms.ModelForm):
    class Meta:
        model = Cinema
        fields = ['name', 'address', 'phone', 'number_halls', 'halls_detal']

class CinemaHall(forms.ModelForm):
    class Meta:
        model = Hall
        fields = ['cinema_name', 'time', 'price', 'format', 'rows', 'places']

# class RegisterForm(UserCreationForm):
#     class Meta:
#         model = MyUser
#         fields = ['username','email','password1','password2','age']