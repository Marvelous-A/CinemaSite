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


admin.site.register(Film, FilmView)
admin.site.register(Category)
admin.site.register(Director)
admin.site.register(Cinema)
admin.site.register(Screening)
admin.site.register(Booking)
admin.site.register(Hall)
admin.site.register(Profile, ProfileView)
admin.site.register(Payment)
admin.site.register(MenuItem)