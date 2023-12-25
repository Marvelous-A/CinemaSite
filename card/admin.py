from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from card.models import Film, Cinema, Hall, CustomUser
#Register your models here.

admin.site.register(Film)
admin.site.register(Cinema)
admin.site.register(Hall)
admin.site.register(CustomUser, UserAdmin)