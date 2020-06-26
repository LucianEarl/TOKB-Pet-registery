from django import forms
from .models import Pet
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30)
    lastname = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=200)

    class Meta:
        model = User
        fields = ('username','lastname', 'email', 'password1', 'password2', )


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ('pet_name', 'species', 'age', 'sex', 'colour','eye_colour','markings','missing')
