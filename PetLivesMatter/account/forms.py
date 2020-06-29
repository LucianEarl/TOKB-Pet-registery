from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from account.models import Account


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=60, help_text='Required. Please put in your email.')
    physical_address = forms.CharField(max_length=300)
    phone_number = forms.CharField(max_length=7)

    class Meta:
        model = Account
        fields = ('username', 'first_name', 'last_name', 'email', 'physical_address', 'phone_number', 'password1', 'password2', )
