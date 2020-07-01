from django.shortcuts import render, redirect
from django.views import generic
from django.http import HttpResponse
from django.http import Http404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import PetForm
from .models import Pet
from account.models import Account
# from .models import Image
# from .forms import ImageForm
# from django.contrib.auth.models import User



def home_screen_view(request):
    context = {}
    accounts = Account.objects.all()
    context['accounts'] = accounts
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

def donate(request):
    return render(request, 'donate.html')

def pet_register_view(request):
    lastimage= Pet.objects.last()

    imagefile= lastimage.imagefile

    form = PetForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        pet = form.save(commit=False)
        pet.owner =  request.user
        pet.save()
        return redirect('my_pets')
    return render(request, 'pet_register.html', {'imagefile': imagefile, 'form': form})

class MyPetListView(generic.ListView):
    model = Pet
    template_name = 'my_pets.html'

class PetDetailView(generic.DetailView):
    model = Pet
    template_name = 'pet_detail.html'
