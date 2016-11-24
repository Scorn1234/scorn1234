from django.shortcuts import render
from django.contrib.auth.middleware import get_user
from django.http import HttpResponseRedirect

from .forms import pet_creation_form
from .models import *
# Create your views here.


def show_pets(request):
    pet_objs = Pet.objects.filter(owner = get_user(request))
    pets = []
    
    for pet in pet_objs:
        temp = pet.__dict__
        temp['photo'] = pet.photo.url
        pets.append(temp)


    return render(request, 'pets/show_pets.html', {
        'pets':pets,
    })
    
    
def add_pet(request):
    form = pet_creation_form(request.POST or None, request.FILES or None)

    if request.method == 'POST' and form.is_valid():
        pet = form.save(commit=False)
        pet.owner = get_user(request)
        pet.save()
        return HttpResponseRedirect('/pets/profile')

    else:
        return render(request, 'pets/add_pet.html', {'form':form})