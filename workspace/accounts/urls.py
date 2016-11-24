from django.conf.urls import url
from . import views


urlpatterns = [
    # 가입
    url(r'regist', views.register, name='regist'),
    # 로그인
    url(
        r'login',
        'django.contrib.auth.views.login',
        name='login',
        kwargs={
            'template_name': 'accounts/login.html'
        }
    ),
    
    url(
        r'logout',
        'django.contrib.auth.views.logout',
        name='logout',
        kwargs={
            'next_page': '/accounts'}
    ),
    
    
    url(r'user/update', views.update_user),
    
    url(r'sitter/add', views.add_sitter),
    url(r'sitter/edit', views.edit_sitter),
    

    url(r'$', views.account_page),
    
    

]