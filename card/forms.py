from django import forms
from .models import Film, Cinema, Hall, CustomUser
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, User

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
    
class CustomUserForm(UserCreationForm):
    phone = forms.CharField(max_length=15, required=False)
    city = forms.CharField(widget=forms.Textarea, required=False)
    date_birth = forms.DateField(required=False)
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
    
    def save(self,commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            CustomUser.objects.create(
                user=user, 
                phone_number=self.cleaned_data['phone_number'], 
                city=self.cleaned_data['city'], 
                date_birth=self.cleaned_data['date_birth'])
        return user