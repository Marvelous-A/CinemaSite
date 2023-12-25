from .models import CustomUser, User
from django.dispatch import receiver
from django.db.models.signals import post_save

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instace, created, **kwargs):
    if created:
        CustomUser.objects.create(user=instace)
    instace.customuser.save()