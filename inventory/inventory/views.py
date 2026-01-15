from django.http import HttpResponse
#added
from django.shortcuts import render, redirect
#for login purpose
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout


"""
to render the  html webpages from template
"""
from django.template.loader import render_to_string
from django.db import connection
from products.models import product


import random


def home_view(request, *args, **kwargs):
    

    return render(request,"home.html")


def menu_view(request,id = None, *args, **kwargs):
    num = random.randint(1,2)
    prod = product.objects.get(id = num)
    #abt = about.objects.get(id)
    prod_list = product.objects.all()

    #Dictionaries for template - abt_temp

    prod_dict = {
        "prod": prod_list,
        "Product_no": prod.Product_no,
        "id": prod.id,
        "Product_name": prod.Product_name,
    }




    return render(request,"menu.html", context=prod_dict)
        
    