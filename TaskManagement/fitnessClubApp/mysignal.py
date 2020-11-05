from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from fitnessClubApp.models import UserProfile
from django.db import models
from time import strftime

@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwarg):
    if created:
        UserProfile.objects.create(User=instance)
    else:
        pass
    