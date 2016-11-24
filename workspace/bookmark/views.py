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
    try:
        marks = Bookmark.objects.filter(user = request.user)
        postings = [ mark.post for mark in marks ]
    except TypeError: # 로그인하지 않은 유저의 요청
        return render(request, "accounts/login.html", {
            'message' : '로그인한 유저만 북마크를 볼 수 있습니다',
        })
    return show_list(request, postings, False)



def add_bookmark(request, post_id, move):
    try:
        user = get_user(request)
        post = Post.objects.get(id = int(post_id))
        
        try:
            bookmark = Bookmark.objects.create(
                user = user,
                post = post,
                )
        except IntegrityError: #이미 등록된 찜글일 때
            Bookmark.objects.get(
                user = user,
                post = post,
                ).delete()
    except : #로그인하지 않은 유저일때 - show_bookmark에서 알아서 해줌
        return render(request, "accounts/login.html", {
            'message' : '로그인한 유저만 북마크할 수 있습니다',
        })
    
    if move=="True":
        return HttpResponseRedirect("/bookmark")
    else : 
        return HttpResponseRedirect("/posting/id={}".format(post_id))
