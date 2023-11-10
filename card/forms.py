from django import forms
from .models import Film
from django.contrib.auth.forms import UserCreationForm
from .models import MyUser

class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ['title', 'img_url','discription', 'year', 'country', 'director', 'duration']


class RegisterForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ['username','email','password1','password2','age']