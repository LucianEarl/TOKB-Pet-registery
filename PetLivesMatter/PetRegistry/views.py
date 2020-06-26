from django.shortcuts import render, redirect
from django.views import generic
from django.http import HttpResponse
from django.http import Http404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, PetForm
from .models import Pet
# from django.contrib.auth.models import User



def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def donate(request):
    return render(request, 'donate.html')

def signup_view(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


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
