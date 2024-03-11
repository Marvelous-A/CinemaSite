from django import forms
from .models import Film, Cinema, Hall, Profile, Payment, User, Category, Director
from django.contrib.auth.forms import UserCreationForm

class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ['title', 'img_url','discription', 'year', 'country', 'director', 'duration', 'cinemas_detals']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_id', 'category_name', 'category_discription']

class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = ['director_name', 'director_id']

class CinemaForm(forms.ModelForm):
    class Meta:
        model = Cinema
        fields = ['id', 'name', 'address', 'phone', 'number_halls', 'fk_cinema_halls']
class CinemaHall(forms.ModelForm):
    class Meta:
        model = Hall
        fields = ['id', 'cinema_name', 'price', 'format', 'rows', 'places']

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone_number', 'birth_date', 'city')

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['brone_places', 'resault_price']

class FilterForm(forms.Form):
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Категории"
    )
    directors = forms.ModelMultipleChoiceField(
        queryset=Director.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Режисеры"
    )

# class DirectorFilterForm(forms.Form):
#     directors = forms.ModelMultipleChoiceField(
#         queryset=Director.objects.all(),
#         widget=forms.CheckboxSelectMultiple,
#         required=False
#     )