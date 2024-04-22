from django.contrib import admin
from card.models import *
from django.contrib.admin import ModelAdmin
#Register your models here.

class FilmView(ModelAdmin):

    list_display = ['pk', 'title', 'discription', 'director_view']

    search_fields = ['discription', 'title']

    list_filter = ['year','director']
    
    empty_value_display = 'Не задано'


    @admin.display(ordering=['director'])
    def director_view(self, obj):
        return obj.director


class ProfileView(ModelAdmin):
    list_display = ['user','phone_number', 'birth_date']
    empty_value_display = 'Не задано'

    def user_view():
        ...

class ScreeningView(ModelAdmin):
    list_display = ['film', 'cinema', 'hall', 'start_time']
    empty_value_display = 'Не задано'
    list_filter = ['cinema', 'film']

class BookingView(ModelAdmin):
    list_display = ['user', 'position', 'cinema', 'hall', 'film']
    empty_value_display = 'Не задано'
    list_filter = ['cinema', 'film']

admin.site.register(Film, FilmView)
admin.site.register(Category)
admin.site.register(Director)
admin.site.register(Cinema)
admin.site.register(Screening, ScreeningView)
admin.site.register(Booking, BookingView)
admin.site.register(Hall)
admin.site.register(Profile, ProfileView)
admin.site.register(Payment)
admin.site.register(MenuItem)