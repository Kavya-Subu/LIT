from django.db import models
from django.utils import timezone
from django.db.models import Q
from django.conf import settings

# Create your models here.

class product_qs(models.QuerySet):
    def search(self, q = None):
        if q is None or q == "":
            return self.none() 
        lookups = Q(Product_no__icontains = q ) |Q(Product_name__icontains = q ) |Q(Product_type__icontains = q )| Q(color__icontains = q )
        return self.filter(lookups)

class productManager(models.Manager):
   def get_queryset(self):
      return product_qs(self.model, using=self._db)
   
   def search(self, q = None):
      return  self.get_queryset().search(q = q)

class product(models.Model):
    Product_no = models.CharField(
        max_length = 10,
        null=False,
        unique=True,
       
    )
    Product_name = models.CharField(
        max_length = 50,
        null=False,
        
    )
    color = models.CharField(
        max_length = 50,
        null=False,
        default=""
    )

    Product_type = models.CharField(
        max_length = 80,
        null=False,
        default="Misc"  
    )
    qty = models.PositiveIntegerField(
        null=False,
        default=0
       
    )
    added_on = models.DateTimeField(auto_now_add = True)
    last_updated = models.DateTimeField(auto_now = True)

    objects = productManager()

