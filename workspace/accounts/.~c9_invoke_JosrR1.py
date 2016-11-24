from django.shortcuts import render
from django.contrib.auth.models import User # 유저모델 가져오기
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.middleware import get_user
from django.template import RequestContext

from .models import *
from .forms import *

import dami_settings as myModule

def account_page(request):
    try:
        user = get_user(request)
        photo = myModule.get_userimg(user)
    except:
        return HttpResponseRedirect('/accounts/login')
    
    if user.is_authenticated():
        try:
            Sitter.objects.get(user_id = user)
            is_sitter = True
        except:
            is_sitter = False
        
    return render(request, 'accounts/mypage.html', {
        'user': user, 
        'photo':photo,
        'is_sitter' : is_sitter,
    })



def register(request):
    user_form = UserCreateForm(request.POST or None, request.FILES or None)
    image_form = ImageCreateForm(request.POST or None, request.FILES or None)

    if request.method == 'POST' and user_form.is_valid() and image_form.is_valid():
        user = user_form.save()
        img = image_form.save(commit=False)
        img.user = user
        img.save()
        return HttpResponseRedirect('accounts/login.html')
        
    return render(request, 'accounts/register.html', {'form': user_form, 'image_form':image_form})
"""-------------img----------------- """
def edit_image(request):
    info = UserImage.objects.get(user_id = get_user(request))
    form = ImageCreateForm(request.POST or None, instance = info)

    if request.method == 'POST' and form.is_valid():
        image = form.save(commit=False)
        UserImage.user_id = get_user(request)
        image.save()
        return HttpResponseRedirect("/accounts")

    return render(request, 'accounts/sitter_manage.html', {
        'form':form,
        'is_add':False,
    })
"""-------------------------------------"""
def edit_user(request):
    info = User.objects.get(user_id = get_user(request))
    user_form=UserCreateForm(request.POST or None, instance = info)
    image_form = ImageCreateForm(request.POST or None, instance = info)
    
    if request.method == 'POST' and user_form.is_valid() and image_form.is_valid():
        user = user_form.save()
        img = image_form.save(commit=False)
        img.user = user
        img.save()
        return HttpResponseRedirect('/accounts')
        
    return render(request, 'accounts/sitter_manage.html', {'form': user_form, 'image_form':image_form, 'is_add':False})




def add_sitter(request):
    form = SitterCreateForm(request.POST or None, request.FILES or None)
    
    if request.method == 'POST' and form.is_valid():
        sitter = form.save(commit=False)
        sitter.user_id = get_user(request)
        sitter.save()
        return HttpResponseRedirect("/accounts")
    
    return render(request, 'accounts/sitter_manage.html', {
        'form': form,
        'is_add':True,
    })
        

        
def edit_sitter(request):
    info = Sitter.objects.get(user_id = get_user(request))
    form = SitterCreateForm(request.POST or None, instance = info)

    if request.method == 'POST' and form.is_valid():
        sitter = form.save(commit=False)
        sitter.user_id = get_user(request)
        sitter.save()
        return HttpResponseRedirect("/accounts")

    return render(request, 'accounts/sitter_manage.html', {
        'form':form,
        'is_add':False,
    })
    
    






        user = User.objects.get