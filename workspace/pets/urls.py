from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'profile', views.show_pets),
    url(r'add', views.add_pet),
]