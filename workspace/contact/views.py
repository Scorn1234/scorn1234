from django.shortcuts import render
from django.contrib.auth.middleware import get_user
from django.http import HttpResponse, HttpResponseRedirect
import datetime
import os

from accounts.models import Sitter
from .models import Contact
from .forms import *

import dami_settings as myModule

def send_message(phone_number, message):
    message = "[맡긴다] " + message
    
    os.system("python send_sms.py {0} {1}".format(phone_number, message))


def send_miss_you(request, contact_id, message):
    contact = Contact.objects.get(id = int(contact_id))
    phone_number = contact.sitter.phoneNumber
    message = "예약자 '{0}'님이 아이가 잘 있는지 궁금해 합니다. 사진을 보내주세요!".format(get_user(request))
    send_message(phone_number, message)
    
    return HttpResponseRedirect("/contact")



def accept_contact(request, contact_id):
    contact = Contact.objects.get(id = int(contact_id))
    contact.status = "reserve"
    contact.save()
    return HttpResponseRedirect("/contact/as_sitter")
    

def cancel_contact(request, contact_id):
    contact = Contact.objects.get(id = int(contact_id))
    contact.status = "cancel"
    contact.save()
    
    phone_number = contact.sitter.phoneNumber
    message = "예약자 '{0}'님이 예약을 취소했습니다".format(get_user(request))
    send_message(phone_number, message)
    
    return HttpResponseRedirect("/contact")



def create_contact(request, form, post):
    if form.is_valid():
        contact = form.save(commit=False)
        contact.sitter = post.author
        contact.owner = get_user(request)
        contact.save()
        
        for species in form.cleaned_data['species_of_animal']:
            contact.species_of_animal.add(species)
        contact.save()

        send_message(contact.sitter.phoneNumber, "새로운 예약 요청이 들어왔습니다. 지금 확인해보세요.")
        
        payment = post.daily_payment*contact.number_of_animal*(contact.end_date - 
            contact.start_date + datetime.timedelta(days=1)).days
        message = "{}원 결제됩니다".format(payment)
        return HttpResponseRedirect("/contact/{}".format(message))


# 유저로서 남긴것 : 시터이름, 시터사진, 별점, 주소, 컨택날짜
def show_conatct_as_owner(request, message=None):
    try:
        Sitter.objects.get(user_id = get_user(request))
        is_sitter = True
    except:
        is_sitter = False
        
    print("메세지", message)

    contacts = Contact.objects.filter(owner = get_user(request))
    
    contact_info = []
    for contact in contacts:
        temp = contact.__dict__
        temp['photo'] = myModule.get_userimg(contact.sitter)
        temp['sitter'] = contact.sitter
        temp['score'] = myModule.get_sitter_score(contact.sitter)
        contact_info.append(temp)

    return render(request, 'contact/contact_list.html', {
        'contacts':contact_info,
        'owner_contact':True,
        'is_sitter' : is_sitter,
        'message' : message,
    })


# 시터로서 들어온것 : 유저이름, 유저사진, 동물종류, 마리수, 요청사항, 컨택날짜, 
def show_conatct_as_sitter(request):
    contacts = Contact.objects.filter(sitter = Sitter.objects.get(user_id=get_user(request)))
    
    
    contact_info = []
    for contact in contacts:
        temp = contact.__dict__
        temp['photo'] = myModule.get_userimg(contact.sitter)
        temp['sitter'] = contact.sitter
        temp['score'] = myModule.get_sitter_score(contact.sitter)
        temp['species_of_animal'] = [ str(i) for i in Species.objects.filter(contact = contact.id)]

        contact_info.append(temp)
    return render(request, 'contact/contact_list.html', {
        'contacts':contact_info,
        'is_sitter' : True,
    })
    
    
    # 맡긴 내역 [<Contact: admin와 user1의 컨택>, <Contact: admin와 user1의 컨택>]
    # [<Species: 고양이>, <Species: 소동물>]
    # [<Species: 파충류>]

    
# 시터사진, 이름, 주소, 컨택날짜
def review(request, contact_id=1):
    form = ReviewForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            contact = Contact.objects.get(id = contact_id)
            Review = form.save(commit=False)
            Review.contact = contact
            contact.status = 'end'
            contact.save()
            Review.save()
            return HttpResponseRedirect('/contact')
        else:
            return HttpResponse(form.errors)
    else:
        try:
            Review.objects.get(contact = contact_id)
            return HttpResponse("이미 리뷰를 등록했습니다.")
        except:
            pass
        
    contact = Contact.objects.get(id = int(contact_id))
    photo = myModule.get_userimg(contact.sitter)
    sitter = contact.sitter
    form = ReviewForm()
    
    return render(request, 'contact/review.html', {
        'contact':contact,
        'photo':photo,
        'form':form,
        'sitter':sitter,
    })
    
    
    
    
    
    
    
    
    
    
    
def show_contact_detail(request, contact_id):
    
    return render(request, 'contact/contact_detail.html', {
    })
    
    
    # 맡긴 내역 [<Contact: admin와 user1의 컨택>, <Contact: admin와 user1의 컨택>]
    # [<Species: 고양이>, <Species: 소동물>]
    # [<Species: 파충류>]
    
    