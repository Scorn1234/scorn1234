from django.conf.urls import url
from . import views
from django.conf import settings


urlpatterns = [
    url(r'(?P<post_id>[0-9]+)/(?P<move>[a-zA-Z]*)', views.add_bookmark),
    url(r'$', views.show_bookmark),
]