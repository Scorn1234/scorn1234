from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.middleware import get_user
from django.db import IntegrityError

from .models import Bookmark
from posting.models import Post
from posting.views import show_list
from accounts.models import Sitter, UserImage
from django.contrib.auth.models import User


def show_bookmark(request):
    message = None
    try:
        marks = Bookmark.objects.filter(user = request.user)
        postings = [ mark.post for mark in marks ]
    except TypeError: # 로그인하지 않은 유저의 요청
        message = '로그인해야 북마크한 글을 볼 수 있습니다'
        return HttpResponseRedirect("/accounts/login") #오픈시 이걸로 바꿔줭
    return show_list(request, postings, message, False)



def add_bookmark(request, post_id, move):
    try:
        bookmark = Bookmark.objects.create(
            user = get_user(request),
            post = Post.objects.get(id = int(post_id))
            )
    except IntegrityError: #이미 등록된 찜글일 때
        Bookmark.objects.get(
            user = get_user(request),
            post = Post.objects.get(id = int(post_id))
            ).delete()
    except : #로그인하지 않은 유저일때
        return HttpResponseRedirect("/accounts")
    
    if move=="True":
        return HttpResponseRedirect("/bookmark")
    else : 
        return HttpResponseRedirect("/posting/id=")
