from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


# Create your models here.

class Sitter(models.Model):
    user_id = models.OneToOneField(settings.AUTH_USER_MODEL)
    gender = models.CharField(max_length=10)
    dwelling = models.CharField(max_length=100)
    has_yard = models.BooleanField(default = False)
    phoneNumber = models.CharField(max_length=12)
    address = models.CharField(max_length=300)
    
    def __str__(self):
        return str(self.user_id)
        

class UserImage(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    photo = models.ImageField(upload_to="usergalary", default="/media/usergalary/default_profile.png")
    
    def save(self, *args, **kwargs):
        try:
            this = UserImage.objects.get(id = self.id)
            if this.photo != self.photo:
                this.photo.delete(save=False)
        except: pass
        super(UserImage, self).save(*args, **kwargs)
        
    def __str__(self):
        return str(self.user)
    
