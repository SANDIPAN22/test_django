from django import forms
from my_app.models import userProfileInfo
from django.contrib.auth.models import User

class userForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model=User
        fields=('username','email','password')

class userProfileInfoForm(forms.ModelForm):
    class Meta():
        model=userProfileInfo
        fields=('portfolio_link','profile_pic')