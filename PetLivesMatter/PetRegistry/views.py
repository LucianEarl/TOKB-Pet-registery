from django.shortcuts import render

# Create your views here.
def home(request):
    pets = Pet.objects.all()
    return render(request, 'home.html')
