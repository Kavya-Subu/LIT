
#added
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import (
    reg_form,
    reg_form2,
    # login_form,
)
from .models import Account
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required



# Create your views here.
# User = settings.AUTH_USER_MODEL
def login_view(request):
    
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        # form = login_form(request.POST or None)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/menu')
        else:
            print('invalid user')
    else:
        form = AuthenticationForm(request)
        # form = login_form(request)
    context = {
        "form" : form
    }
    return render(request,"login.html", context = context)


def reg_view(request):
    
    # form = UserCreationForm(request.POST or None)
    form =reg_form(request.POST or None) 
   
    context = {
        "form" : form,
        # "form2" : form2,
        # "object" : user_obj
    }
    if form.is_valid() :
        user_obj  = form.save() 
        # form2.save()
        return redirect('/reg2')
    
    return render(request,"reg.html", context = context)


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect("/login/")
    
    return render(request,"logout.html", {})


def reg2_view(request):
    
    
    # obj = get_object_or_404(Account, User = request.user)
    form =reg_form2(request.POST or None) 
    
    context = {
        "form" : form,
        # "object" : obj
    }
    if form.is_valid() :
       
        form.save()
        return redirect('/login')
    
    return render(request,"reg2.html", context = context)