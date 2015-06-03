from django.db import models
from django.contrib.auth.models import User
import datetime, pytz

class FBUser(User):
    nickname = models.CharField(blank=True, null=True, max_length=100)
    birthday = models.DateField(blank=True, null=True)
    image = models.FileField(upload_to='images/users/', blank=True, null=True)
    followers = models.ManyToManyField("self")
    lastget = models.DateTimeField(default=datetime.datetime(2015, 1, 1, 0, 0, 0).replace(tzinfo=pytz.utc).astimezone(pytz.timezone("Asia/Tehran")))
    
    def __str__(self):
        return self.username
