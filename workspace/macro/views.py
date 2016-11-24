from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth.models import *
from accounts.models import *
from contact.models import *
from posting.models import *
from pets.models import *

import random
import datetime
import dami_choices

def create_user_set(username, pw, email, photo):
    user = User.objects.create_user(
        username=username,
        email=email,
        password=pw,
        )
        
    image = UserImage.objects.create(
        user = user,
        photo = photo,
        )


def create_user_set_macro(request):
    for i in range(1,51):
        username = "user{}".format(i)
        pw = "emfdjdhwlak".format(i)
        email = "user{}@gmail.com".format(i)
        photo = "/media/usergalary/user{}.jpg".format(i)
        
        create_user_set(username, pw, email, photo)
    return HttpResponse("성공!")



def create_sitter(username):
    sitter = Sitter.objects.create(
        user_id = User.objects.get(username = username),
        gender = random.choice(dami_choices.GENDER)[0],
        dwelling = random.choice(dami_choices.DWELLING)[0],
        has_yard = random.choice(dami_choices.HAS_YARD)[0],
        phoneNumber = "01084332362",
        address = random.choice(dami_choices.ADDRESS),
        )
    
    
#시터 야드 변경
# user = User.objects.get(username = username)
# sitter = Sitter.objects.get(user_id = user)
# sitter.has_yard = random.choice(dami_choices.HAS_YARD)[0]
# sitter.save()



def create_sitter_macro(request):
    for i in range(1,51,2):
        create_sitter("user{}".format(i))
    return HttpResponse("성공!")
    


def species_list_to_str(species):
    return ", ".join(map(str, species))
    

def create_post(sitter):
    species = [ i for i in Species.objects.all()]
    species = random.sample(species, random.randint(1,5))
    
    start_date = datetime.date.today() + datetime.timedelta(days = random.randint(-5, 10))
    post = Post.objects.create(
        author = sitter,
        title = "{}맡아드려요".format(", ".join(map(str, species))),
        text = "안녕하세요. 믿을 수 있는 시터 {}입니다. 댁의 아이들을 가족같이 돌보겠습니다".format(sitter),
        start_date = start_date,
        end_date = start_date + datetime.timedelta(days = random.randint(2, 40)),
        daily_payment = random.randint(10, 30)*1000
        )
    
    for choice in species:
        post.species_of_animal.add(choice)
    post.save()    

    
def create_post_macro(request):
    sitters = Sitter.objects.all()
    for sitter in sitters:
        create_post(sitter)


pet_no = 0
def create_pet(userobj):
    global pet_no
    types = {'개/강아지': 'dog',
        '고양이': 'cat',
        '토끼' : 'rabbit',
        '소동물' : 'small_animal',
        '파충류' : 'reptile',
    }
    features = (
        "사람을 좋아합니다",
        "잘 뭅니다",
        "많이 먹습니다",
        "병이 있습니다",
        "종종 짖습니다",
        "만지는걸 싫어합니다"
    )
    

    numpet = random.randint(1,2)
    
    for _ in range(numpet):
        pet = Pet.objects.create(
            owner = userobj,
            name = "pet {}".format(pet_no),
            animal_type = random.choice(dami_choices.SPEICES_OF_ANIMAL)[0],
            sex = random.choice(dami_choices.SEX_OF_ANIMAL)[0],
            birth_date = datetime.date.today() - datetime.timedelta(days = random.randint(30, 2000)),
            feature = random.choice(features),
            photo = ""
            )
        pet_no+=1
        
        pet.photo = "/media/petgalary/{0}/{0}{1}.jpg".format(
            types[pet.animal_type], random.randint(1, 16))
        pet.save()

def create_pet_macro(request):
    global pet_no
    pet_no = 0
    users = User.objects.all()
    for user in users:
        create_pet(user)
    


def main(request):
    return render(request, 'macro/macro.html', {})

