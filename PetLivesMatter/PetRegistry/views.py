from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.http import HttpResponse
from django.http import Http404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import PetForm
from .models import Pet
from account.models import Account
# from django.contrib.auth.models import User

"""
"""
def pet_detail(request, pk):
    Pet = get_object_or_404(Pet, pk=pk)
    return render(request, 'Pet_detail.html', ['pet': Pet])
"""
"""

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
    form = PetForm(request.POST or None)
    if form.is_valid():
        pet = form.save(commit=False)
        pet.owner =  request.user
        pet.save()
        return redirect('my_pets')
    return render(request, 'pet_register.html', {'form': form})

class MyPetListView(generic.ListView):
    model = Pet
    template_name = 'my_pets.html'

class PetDetailView(generic.DetailView):
    model = Pet
    template_name = 'pet_detail.html'
