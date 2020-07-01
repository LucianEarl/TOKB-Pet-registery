from django import forms
# from django.forms import Form, # ChoiceField
from .models import Pet
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ('imagefile', 'pet_name', 'species', 'age', 'sex', 'colour','eye_colour','markings')

# class MissingPetForm(forms.ModelForm):
#     class Meta:
#         model = Pet
#         fields = ('missing')
class MissingPetForm(forms.Form):
    Pet_missing = forms.BooleanField()

# class FilterForm(Form):
#     FILTER_CHOICES = (
#         ('species', 'Species'),
#         ('age', 'Age'),
#         ('colour', 'Coulour'),
#         ('eye_colour', 'Eye Colour'),
#     )
#     filter_field = ChoiceField(choices=FILTER_CHOICES)
