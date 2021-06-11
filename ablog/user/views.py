from django.shortcuts import render,redirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.urls import reverse_lazy

# Create your views here.
class user(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration.html'
    success_url = reverse_lazy('user:login')

def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        # else:
        #     messages.info(request,'invalid details')
        #     return redirect('user:login')
    else:
        return render(request,"login.html")