"""Self Created..."""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.views.generic.base import RedirectView
from fitnessClubApp import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path( '' ,views.goto, name='goto'),
    path('home/', views.home, name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='/home'), name='logout'),
    path('payt/',views.payt, name='payt'),
    path('post/',views.post, name='post'),
    path('post3/',views.gym, name='post3'),    
    path('prec/',views.prec, name='prec'),
    path('payment_method/',views.payt, name='goto1'),
    path('trainer/', views.trainer, name='lol_Teacher'),
    path('Developer/',views.Developer, name='info'),
    path('history/',views.history, name='history'),
    path('fitness/',views.nav, name='fitness'),
    path('fitness1/',views.nav1, name='fitness1'),
    path('gympost/',views.gym, name='gympost'),
    path('meditationpost1/',views.med, name='meditationpost1'),
    path('meditationpost2/',views.med1, name='meditationpost2'),
    path('yogapost/',views.yoga, name='yogapost'),
    path('yogapost1/',views.yoga1, name='yogapost1'),
    path('dancepost/',views.dance, name='dancepost'),
    path('dancepost1/',views.dance1, name='dancepost1'),
    path('arbicpost/',views.arbic, name='arbicpost'),
    path('eventpost/',views.event, name='eventpost'),
    path('ditepost/',views.dite, name='ditepost'),
    path('paidpost/',views.paid, name='paidpost'),
    path('nointernet/',views.nointer, name='nointernet'),
    path('GYMTrainer/',views.gym_t, name='GYMTrainer'),
    path('befit/',views.befit, name='befit')
    
    
]
