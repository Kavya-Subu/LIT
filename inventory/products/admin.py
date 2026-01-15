from django.contrib import admin

# Register your models here.
from .models import product

class productAdmin(admin.ModelAdmin):
    list_display = ['id', 
    'Product_no', 
    'Product_name',
    'color',
    'Product_type',
    'qty', 
    'added_on', 
    'last_updated'
    ]
    search_fields = ['id', 'Product_no', 'Product_name']

admin.site.register(product, productAdmin)