"""petsitter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + [
    url(r'^1', include('home.urls')),
    url(r'^2', include('bookmark.urls')),
    url(r'^3', include('posting.urls')),
    url(r'^4', include('accounts.urls')),

    
    url(r'^admin', admin.site.urls),
    url(r'^macro', include('macro.urls')),

    url(r'^accounts', include('accounts.urls')),
    
    url(r'^bookmark', include('bookmark.urls')),
    
    url(r'^posting', include('posting.urls')),
    url(r'^map', include('map.urls')),
    
    url(r'^contact', include('contact.urls')),
    
    url(r'^pets', include('pets.urls')),
    
    url(r'^home', include('home.urls')),


    url(r'^', include('home.urls')),
]