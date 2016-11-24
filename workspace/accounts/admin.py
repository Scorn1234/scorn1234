from django.contrib import admin

# Register your models here.
from .models import Sitter, UserImage

"""
계정과 관련된 앱입니다.
계정 생성, 탈퇴, 로그인, 로그아웃이 가능합니다.

계정 생성 : 
url : accounts/new/(?P<user_id>[0-9]+)/(?P<user_pw>[0-9]+)
view : <id,pw,pw_confirm>을 입력받아 DB에 등록합니다.


탈퇴 : 
아직 구현중입니다.

로그인 : 
url : accounts/login
view : <id,pw>를 입력받아 로그인합니다.

로그아웃 : 
url : accounts/logout
view : <id>를 입력받아 로그아웃합니다.

"""

admin.site.register(Sitter)
admin.site.register(UserImage)
