from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'1', views.show_1),
    url(r'2', views.show_2),
    url(r'3', views.show_3),
    url(r'^', views.show_home),
]