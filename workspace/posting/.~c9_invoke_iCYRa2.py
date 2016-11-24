from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from operator import __or__ as OR
from copy import deepcopy

# accounts
from django.contrib.auth.models import User
from accounts.models import Sitter, UserImage
from django.contrib.auth.middleware import get_user

# bookmark
from bookmark.models import Bookmark

# contact
from contact.models import *
from contact.forms import ContactForm
from contact.views import create_contact

#posting
from .models import Post
from .forms import *

import dami_settings as myModule


def search_post(request):
    form = search_form(request.POST or None, request.FILES or None)
    
    if form.is_valid():
        data = form.cleaned_data
        posts = Post.objects.all()

        #날짜
        try: posts.filter(start_date__let = data['start_date'])
        except: pass
        try : posts.filter(start_date__get = data['end_date'])
        except: pass
        
        
        #정확히 일치, 라디오 셀렉트. 생각해보니 모두 시터랑 관계된 필드로군..
        
        # 선택하지 않으면 ""
        if data['gender'] and data['gender'] != 'all':
            temp_posts, posts = posts, []
            for post in temp_posts:
                if post.author.gender == data['gender']:
                    posts.append(post)


        # 시터 동물 보유 여부. 스트링형태 불리안""
        if data['animal_sitter_own'] and data['animal_sitter_own'] != 'all':
            condition = True if data['animal_sitter_own'] == "True" else False
            temp_posts, posts = posts, []
            for post in temp_posts:
                num = myModule.get_number_of_pet(post.author)
                if ( (condition == True and num != 0) or 
                    ( condition == False and num ==0 ) ) :
                    posts.append(post)


        # 왠지모르게 str로 받아지더라
        if data['has_yard']:
            temp_posts, posts = posts, []
            cond = True if data['has_yard'] == "True" else False
            for post in temp_posts:
                if post.author.has_yard == cond : posts.append(post)

        
        
        #멀티셀렉트. 셀렉트가 없으면 []로 들어옴
        if data['species_of_animal']:
            species_want = data['species_of_animal']
            temp_posts, posts = posts, []
            for post in temp_posts:
                species_on_post = Species.objects.all().filter(post = post)
                if any( [species in str(species_on_post) for species in species_want] ):
                    posts.append(post)                    

        if data['dwelling']:
            dwelling_want = data['dwelling']
            temp_posts, posts = posts, []
            for post in temp_posts:
                if post.author.dwelling in data['dwelling'] :
                    posts.append(post) 
    else:
        return show_post_list(request, message = "시작일은 종료일보다 작아야 합니다")
    return show_list(request, posts)


def show_post_list(request, sitter_id=None, page_number=0, message = None):
    try:
        sitter = Sitter.objects.get(id = sitter_id)
        postings = Post.objects.filter(author = sitter)
    except:
        postings = Post.objects.all().order_by('published_date')
    return show_list(request, postings, message = message)



def show_list(request, post_objects, is_show_post=True, message = None):
    form = search_form(request.POST or None, request.FILES or None)
    
    try : # 검색자가 시터인지 아닌지 파악 - 글쓰기 버튼 활성화
        Sitter.objects.get(user_id = get_user(request))
        is_sitter = True
    except: #(TypeError, AttributeError, ObjectDoesNotExist):
        is_sitter = False
    
    posts = []
    for post_obj in post_objects:
        sitter = post_obj.author
        
        post = post_obj.__dict__
        post['author'] = sitter.__dict__
        post['author']['name'] = str(sitter)
        post['author']['photo'] = myModule.get_userimg(sitter)
        post['author']['score'] = myModule.get_sitter_score(sitter)
        post['author']['score'] = myModule.get_sitter_score(sitter)
        post['author']['number_of_animal'] = myModule.get_number_of_pet(sitter)
        posts.append(post)
    
    return render(request, 'posting/post_list.html', {
        'posts': posts,
        'form': form,
        'is_sitter' : is_sitter,
        'is_show_post' : is_show_post,
        'message' : message,
        
    } )



def showPost(request, post_id):
    post_obj = Post.objects.get(id = int(post_id))
    form = ContactForm(request.POST or None, request.FILES or None, post_id = post_obj)

    if request.method == 'POST' and form.is_valid():
        return create_contact(request, form, post_obj)

    # GET or invalid form
    sitter_obj = post_obj.author
    post = post_obj.__dict__
    post['species_of_animal'] = Species.objects.all().filter(post = post_id)
    post['number_of_animal'] = myModule.get_number_of_pet(sitter_obj.user_id)
    try:
        Bookmark.objects.get(user = get_user(request), post = post_obj)
        post['marked'] = True
    except:
        post['marked'] = False

    sitter = sitter_obj.__dict__
    sitter['name'] = str(sitter_obj)
    sitter['score'] = myModule.get_sitter_score(sitter_obj)
    sitter['photo'] = myModule.get_userimg(sitter_obj)

    return render(request, 'posting/post_detail.html', {
        'post' : post, 
        'sitter':sitter, 
        'form':form,
    } )

    
def addPost(request):
    form = PostForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        post = form.save(commit=False)
        post.author = Sitter.objects.get(user_id = get_user(request))
        post.save()
        
        for species in form.cleaned_data['species_of_animal']:
            post.species_of_animal.add(species)
        post.save()
            
        return HttpResponseRedirect('/posting/id='+str(post.id))

    # request.method == 'GET' or invalid
    return render(request, 'posting/post_add.html', {'form':form, is_} )
        




def editPostList(request, sitter_id=None, page_number=0, message = None):
    form = 


def modPost(request):
    return render(request, 'posting/post_edit_list.html')