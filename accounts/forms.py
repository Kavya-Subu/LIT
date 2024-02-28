from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, AbstractUser
from .models import Account

class reg_form2(forms.ModelForm):
    # gender_choices = {"m":"Male", "f": "Female" }
    dob = forms.DateField(widget=forms.DateInput(attrs={"input type": "date"}))
    # gender = forms.ChoiceField(widget=forms.RadioSelect,choices = gender_choices)
   
    class Meta:
        model = Account
        fields = [
            'User',
            'dob',
            'phone',
            'address',
            'gender',
            'designation',   
        ]
        

class reg_form(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={}))
    class Meta:
        model = User
        fields = ['username', 'first_name','last_name' ,'email','password1', 'password2']
        # field_classes = {'username': UsernameField}
        labels={
           "username": "Username"
        }
        error_messages={
           "username": {
               "required": "Please enter a valid Username for your Account"
            }
       }

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['email'].widget.attrs.update({"placeholders":"johndoe@gmail.com"})
  


      

# class login_form(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = [
#             'username', 
#             'password'
            
#         ]
# class reg_form(forms.ModelForm):
#     class Meta:
#         model = Account
#         fields = [
#             'dob',
#             'gender',
#             'access',
#             'role',
#             'phone',
#             'address',
#             'start_date'
#          ]