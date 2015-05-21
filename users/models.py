from django.db import models
from django.contrib.auth.models import User


class FBUser(User):
    nickname = models.CharField(blank=True, null=True, max_length=100)
