from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def donate(request):
    return render(request, 'donate.html')

# views.py
from django.shortcuts import render, redirect
from .forms import RegisterForm


# Create your views here.
def register(response):
    if response.method == "POST":
	form = RegisterForm(response.POST)
	if form.is_valid():
	    form.save()

	return redirect("/home")
    else:
	form = RegisterForm()

    return render(response, "register/register.html", {"form":form})
