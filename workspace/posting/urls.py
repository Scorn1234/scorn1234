from django.conf.urls import url
from . import views
from django.conf import settings


"""
글 등록 :  /posting/new
글 보기 :  
            /posting/page=숫자. 숫자가 1이면 최근부터 5개까지의 post의 제목과 글id를 보여줍니다.
            /posting/id=숫자. 숫자는 post id입니다. post에 관한 모든 사항을 보여줘야 합니다.
글 제거 : url 제공하지 않습니다. request로 끝냄.


자기 글 편집하는 리스트: /posting/edit
"""


urlpatterns = [
    url(r'(sitter=(?P<sitter_id>[0-9]+)/)?page=(?P<page_number>[0-9]+)', views.show_post_list),
    url(r'postid=(?P<postid>[0-9]+)$', views.editPost),

    url(r'id=(?P<post_id>[0-9]+)$', views.showPost),
    url(r'search', views.search_post),

    url(r'new$', views.addPost),
    url(r'$', views.show_post_list), # 고치면 어플에서 접속 안됨
    
    
]