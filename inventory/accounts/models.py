from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser , BaseUserManager
from datetime import date,datetime


class Account(models.Model):

    User = models.ForeignKey(User, on_delete=models.CASCADE)
    access = models.CharField(
        max_length= 2,
        default= 'NA', 
        null = False
    )
    dob = models.DateField( 
        default= datetime.now(),
        null=False,
        
    )

    phone = models.PositiveIntegerField(
        max_length= 10,
        null = False,
        default='00'

    )
    address = models.TextField(
        max_length= 200,
        null = False,
        default='NA'

    )
    gender = models.CharField(
        choices=[('m','Male'),('f','Female'),('o','others')],
        max_length=10,
        null=False,
        default=[('o','others')]
    )

    designation = models.CharField(
        choices=[
            ('NA','NA'),
            ('im','Inventory Manager'),
            ('fs','Floor Supervisor'),
            ('st','Staff')   
        ],
        max_length=20,
        null = False,
        default=[('NA','NA')]
    )





    def __str__(self):
        return self.User.username
    
#class emp_db(models.Model):
#     User = models.OneToOneField(User, on_delete=models.CASCADE)
#     f_name = models.CharField(
#         max_length= 50,
#         null = False,
#         default='NA'

#     )
#     l_name = models.CharField(
#         max_length= 50,
#         null = False,
#         default='NA'

#     )


