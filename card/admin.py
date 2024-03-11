from django.contrib import admin
from card.models import Film, Cinema, Hall, Profile, Payment, Category, Director
#Register your models here.


admin.site.register(Film)
admin.site.register(Category)
admin.site.register(Director)
admin.site.register(Cinema)
admin.site.register(Hall)
admin.site.register(Profile)
admin.site.register(Payment)