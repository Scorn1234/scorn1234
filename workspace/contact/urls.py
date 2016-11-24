from django.conf.urls import url
from . import views
from django.conf import settings

urlpatterns = [
    
    
    url(r'detail/(?P<contact_id>[0-9]+)', views.show_contact_detail),
    
    
    
    url(r'message/(?P<contact_id>[0-9]+)/(?P<message>.+)', views.send_miss_you),
    
    url(r'accept/(?P<contact_id>[0-9]+)', views.accept_contact),
    url(r'cancel/(?P<contact_id>[0-9]+)', views.cancel_contact),
    
    url(r'review/(?P<contact_id>[0-9]+)', views.review),

    url(r'as_sitter', views.show_conatct_as_sitter),
    url(r'(/(?P<message>.*))?', views.show_conatct_as_owner), #괄호 그대로 둘 것
    
    url(r'detail/(?P<contact_id>[0-9]+)',views.show_contact_detail),
]