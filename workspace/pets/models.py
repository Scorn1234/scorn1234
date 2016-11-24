from django.db import models
from django.utils import timezone

# Create your models here.

class Pet(models.Model):
    '''
    이름, 나이, 종족, 사진, 특이사항
    사진은 용량관계로 나중에 등록할것임
    '''
    owner = models.ForeignKey('auth.User')
    name = models.CharField(max_length=10)
    animal_type = models.CharField(max_length=30)
    sex = models.CharField(max_length=15, default="암컷") #0이면 수컷, 1이면 암컷
    birth_date = models.DateField(
            blank=True, null=True)
    feature = models.TextField()
    photo = models.ImageField(upload_to="petgalary", default="/media/petgalary/default_profile.png")

    def __str__(self):
        return self.name
