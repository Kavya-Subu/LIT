from django.shortcuts import render


# Use the decorator whereever necessery To verify if the user is logged in 
# to not use the default django url path add login url in settings.py
from django.contrib.auth.decorators import login_required

#importing the db structure
from .models import product

#importing forms from  form.py
from .forms import product_form

#importing for advance search
from django.db.models import Q



def product_search_view(request):
    q = request.GET.get('q') 
    qs = product.objects.search(q = q)
        
    context = {
         "obj_list": qs,
    }

    return render(request, "product_search.html", context =context)

# Create your views here.

def product_view(request, id = None):
    Product_no = None
    if id is not None:
        Product_no = product.objects.get(id = id)
    context = {
        "object": Product_no,
    }
    return render(request, "product_detail.html", context = context)

@login_required
def create_view(request):
        #getting the unvalidated data from the UI
        form = product_form(request.POST or None)
        context = {
            "form": form
        }
        #to ensure whether the date is validated
        if form.is_valid():
            create_obj = form.save()
            context ['form'] = about_form()
           

        return render(request, "product_create.html", context = context)


# Create your views here.
