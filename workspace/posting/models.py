from django.db import models
from django.utils import timezone
from datetime import date

from contact.models import Species
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('accounts.Sitter')
    published_date = models.DateField(default = timezone.now)

    title = models.CharField(max_length=200)
    text = models.TextField()
    start_date = models.DateField(default=date.today)
    end_date = models.DateField(default=date.today)
    daily_payment = models.IntegerField(default = 10000)
    species_of_animal = models.ManyToManyField(Species)

    def __str__(self):
        return self.title

