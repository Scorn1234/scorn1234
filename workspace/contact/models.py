from django.db import models
from django.utils import timezone
from datetime import date
from django.contrib.admin.widgets import AdminDateWidget 


import dami_choices as myModule


class Species(models.Model):
    name = models.CharField(max_length = 10, choices = myModule.SPEICES_OF_ANIMAL)
    def __str__(self):
         return self.name

class Contact(models.Model):
    sitter = models.ForeignKey('accounts.Sitter')
    owner = models.ForeignKey('auth.User')
    
    start_date = models.DateField()
    end_date = models.DateField()
    species_of_animal = models.ManyToManyField(Species)
    number_of_animal = models.IntegerField()
    extra_request = models.CharField(max_length=300)
    status = models.CharField(max_length=30, default = "wait")
    
    published_date = models.DateField(default = timezone.now)
        
    def __str__(self):
        return str(self.owner) + "와 " + str(self.sitter) + "의 컨택 : " + str(self.status)


class Review(models.Model):
    contact = models.OneToOneField(Contact)
    score = models.IntegerField(default=5)
    comment = models.CharField(max_length=300)
    
    published_date = models.DateField(default = timezone.now)

    def __str__(self):
        return str(self.contact.owner) + "가 " + str(self.contact.sitter) + "에게 " + str(self.score) + "점을 매겼습니다."
