from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class UserRegisterForm(UserCreationForm):
    email  = forms.EmailField()


    class Meta:
        #which model or database to interact with
        model = User
        #the fields that will be shown on our form and in order
        fields = ['username','email', 'password1', 'password2']





















