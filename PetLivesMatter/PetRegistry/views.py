from django.shortcuts import render, redirect
from django.views import generic
from django.http import HttpResponse
from django.http import Http404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
<<<<<<< HEAD
from .forms import PetForm # FilterForm
=======
from .forms import PetForm, MissingPetForm
>>>>>>> b9ec8a9037dfba4d8a02243fa764f04ae65827e7
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



# class MissingPets(ListView):
#     model = Pet
#     template_name = 'missing_pets.html'
#
#     def is_valid_queryparam(param):
#         return param != '' and param is not None
#
#     def missing_pet_view(request):
#         qs = Pet.objects.all()
#             categories = Pet.objects.all()
#             species = request.GET.get('species')
#             sex = request.GET.get('sex')
#             colour = request.GET.get('colour')
#             eye_colour = request.GET.get('eye_colour')
#
#             if is_valid_queryparam(species)
#                 qs = qs.filter(categories__name=species)
#             if is_valid_queryparam(sex)
#                 qs = qs.filter(categories__name=sex)
#             if is_valid_queryparam(colour)
#                 qs = qs.filter(categories__name=colour)
#             if is_valid_queryparam(eye_colour)
#                 qs = qs.filter(categories__name=eye_colour)
#
#         context = {
#             'queryset' : ps,
#             'categories' : categories
#         }
#         return render(request, 'missing_pets.html', context)



    # def get_queryset(self):
    #     filter_field = self.request.GET.get('filter_field')
    #
    #     return Pet.objects.all()
    #
    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #     context['form'] = FilterForm(initial={
    #         'filter_field': self.request.GET.get('filter_field', ''),
    #     })
    #
    #     return context



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
        pet.owner = request.user
        pet.save()
        return redirect('my_pets')
    return render(request, 'pet_register.html', {'imagefile': imagefile, 'form': form})

class MissingPetsView(generic.ListView):
    model = Pet
    template_name = 'missing_pets.html'

class MyPetListView(generic.ListView):
    model = Pet
    template_name = 'my_pets.html'

def pet_detail_view(request, pk):
    try:
        pet = Pet.objects.get(id = pk)
        # missing_status = pet.missing
        if pet.missing == True:
            form = MissingPetForm(request.POST or None, initial = {'Pet_missing' : 'True'})
        else:
            form = MissingPetForm(request.POST or None, initial = {'Pet_missing' : 'False'})
        # if form.is_valid():
        #     if pet.

    except Pet.DoesNotExist:
        raise Http404('pet not found')

    return render(request, 'pet_detail.html', {'pet': pet, 'form': form})
