from django.contrib import admin
from card.models import Film, Cinema, Hall#, MyUser
#Register your models here.

admin.site.register(Film)
admin.site.register(Cinema)
admin.site.register(Hall)
#admin.site.register(MyUser)