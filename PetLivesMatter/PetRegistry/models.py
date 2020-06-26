from django.db import models
from django.conf import settings

# Create your models here.

class Pet(models.Model):

    SPECIES_CHOICES =(
        ("Dog",
            (
                ("Mutt","Mutt"),
                ("Dalmatian","Dalmatian"),
                ("German Shepherd","German Shepherd"),
                ("Corgie","Corgie"),
                ("Beagle","Beagle"),
                ("Husky","Husky"),
            )
        ),
        ("Cat",
            (
                ("Housecat","Housecat"),
                ("Sphynx","Sphynx"),
                ("Siamese","Siamese"),
                ("Bengal","Bengal"),
                ("Maine Coon","Maine Coon"),
                ("Ragdoll","Ragdoll"),
            )
        ),
        ("Parrot",
            (
                ("Cockatoo","Cockatoo"),
                ("Indian Ringneck","Indian Ringneck"),
                ("Macaw","Macaw"),
                ("Galah","Galah"),
                ("Cockatiel","Cockatiel"),
                ("Conure","Conure"),
            )
        ),
        ("Snake",
            (
                ("Anaconda","Anaconda"),
                ("Rattlesnake","Rattlesnake"),
                ("Cobra","Cobra"),
                ("Asp","Asp"),
                ("Python","Python"),
                ("Sea Snake","Sea Snake"),
            )
        ),
    )

    SEX_CHOICES = (("Female", "Female"),("Male","Male"))
    COLOUR_CHOICES = (("Brown","Brown"),("Black","Black"),("White","White"),
    ("Orange","Orange"),("Green","Green"),("Yellow","Yellow"),("Blue","Blue"))
    pet_name = models.CharField(max_length=30)
    species = models.CharField(max_length=20, choices=SPECIES_CHOICES)
    age = models.PositiveIntegerField()
    sex = models.CharField(max_length = 7, choices=SEX_CHOICES)
    colour = models.CharField(choices = COLOUR_CHOICES, max_length=10)
    eye_colour = models.CharField(choices = COLOUR_CHOICES, max_length=10)
    markings = models.CharField(max_length=250)
    missing = models.BooleanField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.pet_name + ': ' + self.colour + ' ' + self.species
