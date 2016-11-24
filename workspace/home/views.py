from django.shortcuts import render

from posting.views import show_list
from posting.models import *

def show_home(request):
    return render(request, "home/home.html", {})
    
def show_1(request):
    return render(request, "home/tutorial.html", {})

# 소동물    
def show_2(request):
    posts = []
    for post in Post.objects.all():
        if "소동물" in str(Species.objects.all().filter(post = post)):
            posts.append(post)
    return show_list(request, posts)
        

def show_3(request):
    posts = []
    for post in Post.objects.all():
        print(Species.objects.all().filter(post = post))

        if "고양이" in str(Species.objects.all().filter(post = post)):
            posts.append(post)
    return show_list(request, posts)
