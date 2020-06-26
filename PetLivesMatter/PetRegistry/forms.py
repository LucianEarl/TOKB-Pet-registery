
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30)
    lastname = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=200)

    class Meta:
        model = User
        fields = ('username','lastname', 'email', 'password1', 'password2', )


class PetForm():

    class Meta:
        model = Pet
        fields = ('pet_name', 'species', 'age', 'sex', 'colour','eye_colour','markings','missing','owner')

        # SEX_CHOICES = (("F", "Female"),("M","Male"))
        # COLOUR_CHOICES = (("Brown","Brown"),("Black","Black"),("White","White"),
        # ("Orange","Orange"),("Green","Green"),("Yellow","Yellow"),("Blue","Blue"))
        # pet_name = models.CharField(max_length=150)
        # species = models.CharField(max_length=20, choices=SPECIES_CHOICES)
        # age = models.IntegerField()
        # sex = models.CharField(max_length = 7, choices=SEX_CHOICES)
        # colour = models.CharField(choices = COLOUR_CHOICES, max_length=10)
        # eye_colour = models.CharField(choices = COLOUR_CHOICES, max_length=10)
        # markings = models.CharField(max_length=250)
        # missing = models.BooleanField()
        # owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
