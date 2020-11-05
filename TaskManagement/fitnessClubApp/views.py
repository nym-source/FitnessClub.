from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
#import form 
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView
from fitnessClubApp.models import UserProfile

# Create your views here.


class RegisterView(CreateView):
    model = User
    fields = ['username', 'password', 'first_name', 'last_name', 'email']
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.instance.password = make_password(form.instance.password)
        return super().form_valid(form)

    def __str__(self):
        pass  # Do stuff here

class fitdata():
    def pramod(request):
        if 'pname' in request.GET and request.GET['pname']:
            p1 = request.GET['pname']
    
        return render(request,'index.html')
        
            
    

def home(request):
    return render(request,'index.html')

def payt(request):
    return render(request, 'payt.html')
    if request.method=="POST":
        if request.POST.get('gym'):
            savevalue=UserProfile()
            savevalue.gym=request.POST.GET('gym')
            savevalue.save()
            return render(request, 'post.html')
        else:
            return request(request, 'nav.html')
    else:
        return render(request, 'index.html')    

def trainer(request):
    return render(request,'trainer.html')

def Developer(request):
    return render(request,'Developer.html') 

def history(request):
    return render(request,'history.html')

def goto(request):
    return render(request,'goto.html')

def prec(request):
    return render(request,'prec.html')

def post(request):
    return render(request,'gym1.html')

def nav(request):
    return render(request,'fitness.html')

def nav1(request):
    return render(request,'fitness1.html')

def gym(request):
    return render(request,'gym.html')

def med(request):
    return render(request,'medi.html')

def med1(request):
    return render(request,'medi1.html')

def yoga(request):
    return render(request,'yoga.html')

def yoga1(request):
    return render(request,'yoga1.html')

def dance(request):
    return render(request,'dance.html')

def dance1(request):
    return render(request,'dance1.html')

def arbic(request):
    return render(request,'arbic.html')

def event(request):
    return render(request,'event.html')

def dite(request):
    return render(request,'dite.html')

def paid(request):
    return render(request,'nopaid.html')

def nointer(request):
    return render(request,'nonet.html')

def gym_t(request):
    return render(request,'gym2.html')

def befit(request):
    return render(request,'befit.html')

