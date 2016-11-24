from django.contrib import admin

# Register your models here.
from .models import Post

"""
글을 등록, 보기, 제거하는 app입니다.


글 등록 : 
url : posting/new
view : request를 받아 Post model에 해당하는 구조로 만들어 Post를 add합니다.


글 보기 : 
1. 글 목록(제목) 출력
url : posting/page=숫자
view : 만들어진 순서대로 정렬하고, [숫자*5 : 숫자*10+5] post의 제목과 글id를 보여줍니다.


2. 글 내용 출력
url : posting/id=숫자
view : 해당 id를 가진 글을 form에 맞게 전달합니다.


3. 글 제거
아직 만드는 중입니다.
"""

admin.site.register(Post)