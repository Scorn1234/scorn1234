from django.shortcuts import render
from django.contrib.auth.middleware import get_user

from .models import Contact
from .forms import *

import dami_settings as myModule



# 유저로서 남긴것 : 시터이름, 시터사진, 별점, 주소, 컨택날짜

def show_conatct_as_owner(request):
    contacts = Contact.objects.filter(owner = get_user(request))
    contact_info = []
    for contact in contacts:
        temp = contact.__dict__
        temp['photo'] = myModule.get_userimg_by_userobj(contact.sitter)
        temp['sitter'] = myModule.get_userobj_by_name(contact.sitter)
        contact_info.append(temp)
    return render(request, 'contact/contact_list.html', {
        'contacts':contact_info,
        'owner_contact':True
    })


# 시터로서 들어온것 : 유저이름, 유저사진, 동물종류, 마리수, 요청사항, 컨택날짜, 
def show_conatct_as_sitter(request):
    contacts = Contact.objects.fiter(sitter = get_user(request))
    contact_info = []
    for contact in contacts:
        temp = {}
        temp['contact'] = contact
        contact_info.append(temp)
        contact_info.append(temp)
    #return render(request, 'contact/contact_list.html', {contacts:contact_info})    
    # html만들고 주석 풀어줭
    
    
    
# 시터사진, 이름, 주소, 
def show_review_page(request):
    if request.methos == 'POST':
        form = ReviewForm(request.POST)
    else:
        form = ReviewForm()
        return render(request, 'contact/review.html', {
            'form':form
            
            
        })
        
        
