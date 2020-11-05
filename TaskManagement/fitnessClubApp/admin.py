from django.contrib import admin
from .models import fitdata
from fitnessClubApp.models import UserProfile
# Register your models here.

admin.site.register(fitdata)
admin.site.register(UserProfile)
