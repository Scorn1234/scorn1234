from django.contrib.auth.models import User

from accounts.models import Sitter, UserImage
from contact.models import *
from pets.models import *


def get_userimg(userobj):
    try: #유저 오브젝트
        return UserImage.objects.get(user=userobj).photo.url
    except: #시터 오브젝트
        user = User.objects.get(username = userobj)
        return UserImage.objects.get(user=user).photo.url
        

def get_userobj_by_name(username):
    return User.objects.get(username = username)
    
    
def get_sitterobj_by_name(username):
    user = get_userobj_by_name(username = username)
    return Sitter.objects.get(userid = user)
    
    
def get_number_of_pet(obj):
    try: #유저로서
        return Pet.objects.filter(owner = obj).count()
    except: #시터로서
        return Pet.objects.filter(owner = obj.user_id).count()


def get_sitter_score(sitterobj):
    contacts = Contact.objects.filter(sitter = sitterobj)
    score = 0
    try:
        for contact in contacts:
            score += Review.objects.get(contact = contact).score
        return round(score / len(contacts) / 2)
    except:
        return 0



def DBmigration():
    contacts = Contact.objects.all()
    for contact in contacts:
        if contact.start_date <= date.today() <= contact.end_date:
            contact.status = "progress"
            contact.save()
        elif date.today() > contact.end_date:
            contact.status = "complete"
            contact.save()
            
            
#모든 컨택의 상태를 리뷰 전으로 만듦
def tryReview():
    reviews = Review.objects.all()
    for review in reviews:
        review.delete()
    
    contacts = Contact.objects.all()
    for contact in contacts:
        contact.status = "complete"
