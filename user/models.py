from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class BaseUser(AbstractUser):
    email = models.EmailField(unique=True)
    nickname = models.CharField(max_length=50,unique=True,blank=True)
    last_point_at = models.DateTimeField(null=True, blank=True, default=None)
    is_hidden = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
