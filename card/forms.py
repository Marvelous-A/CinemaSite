from django import forms
from .models import Film

class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ['title', 'img_url','discription', 'year', 'country', 'director', 'duration']