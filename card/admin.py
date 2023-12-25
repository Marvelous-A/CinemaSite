from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from card.models import Film, Cinema, Hall, CustomUser, User
#Register your models here.

class CustomUserInline(admin.StackedInline):
    model = CustomUser
    can_delete = False
    verbose_name_plural = 'profile'

class UserAdmin(BaseUserAdmin):
    inlines = (CustomUserInline,)

admin.site.register(Film)
admin.site.register(Cinema)
admin.site.register(Hall)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)