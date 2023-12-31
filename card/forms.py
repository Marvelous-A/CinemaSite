from django import forms
from .models import Film, Cinema, Hall, Profile, Payment

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

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone_number', 'email', 'birth_date', 'city']

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['brone_places', 'resault_price']