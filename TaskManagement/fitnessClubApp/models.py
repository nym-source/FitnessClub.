from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from django import forms


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    model = User
    fields = ('username', 'email', 'password')

    def __str__(self):
        return self.username
    
class UserProfile(models.Model):

    User = models.OneToOneField(to=User, on_delete=CASCADE, null=True)
    position = models.BooleanField(default=False, blank=True)
    gym = models.CharField(max_length=10, blank=True )
    fitness =  models.CharField(max_length=10, blank=True )
    krate = models.CharField(max_length=10,   blank=True )
    yoga =  models.CharField(max_length=10,   blank=True )
    dance =  models.CharField(max_length=10,  blank=True )
    arbic =  models.CharField(max_length=10,  blank=True )
    
    def __str__(self):
        return '%s %s %s %s %s %s %s %s'%(self.User, self.position, self.gym, self.fitness, self.krate, self.yoga, self.dance, self.arbic)
         



# Create your models here.
class fitdata(models.Model):
    Email = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    
    def _user_(self):
        return "%s %s"%(self.Email)
    