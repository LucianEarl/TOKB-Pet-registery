from django import forms
from .models import Pet
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ('pet_name', 'species', 'age', 'sex', 'colour','eye_colour','markings','missing')
