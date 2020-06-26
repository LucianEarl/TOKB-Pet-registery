from django.shortcuts import render, redirect
from django.views import generic
from django.http import HttpResponse
from django.http import Http404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm



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
    form = PetForm(request.POST)
    if form.is_valid():
        form.save()
    #     username = form.cleaned_data.get('username')
    #     password = form.cleaned_data.get('password1')
    #     user = authenticate(username=username, password=password)
    #     login(request, user)
    #     return redirect('home')
    # else:
    #     form = SignUpForm()
    return render(request, 'pet_register.html', {'form': form})
