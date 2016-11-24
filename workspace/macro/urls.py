from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'new_accounts', views.create_user_set_macro),
    url(r'new_sitter', views.create_sitter_macro),
    url(r'new_post', views.create_post_macro),
    url(r'new_pet', views.create_pet_macro),
    url(r'^', views.main),
]