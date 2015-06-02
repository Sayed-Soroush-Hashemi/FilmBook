from django.db import models
from django.contrib.auth.models import User


class FBUser(User):
    nickname = models.CharField(blank=True, null=True, max_length=100)
    birthday = models.DateField(blank=True, null=True)
    image = models.FileField(upload_to='users/images', blank=True, null=True)
    followers = models.ManyToManyField("self")
    
    def __str__(self):
        return self.username
