from django.db import models
from django.utils import timezone
from datetime import date

class Bookmark(models.Model):
    user = models.ForeignKey('auth.User')
    post = models.ForeignKey('posting.Post')
    published_date = models.DateTimeField(default = timezone.now)

    class Meta:
        unique_together = ('user', 'post',)

    def __str__(self):
        return str(self.user)+"가 찜한 "+str(self.post)
