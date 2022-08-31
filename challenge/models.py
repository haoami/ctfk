from django.db import models

# Create your models here.
class Challenge(models.Model):
    pub_date = models.DateTimeField(auto_now=True)
    solved = models.BigIntegerField(default=0)
    title = models.CharField(max_length=256, default="",unique=True)
    content = models.TextField(default="")
    initial_points = models.BigIntegerField(default=0)
    minimum_points = models.BigIntegerField(default=0)
    decay = models.BigIntegerField(default=0)
    flag = models.CharField(max_length=512, default="")
    ChallengeClass=models.CharField(max_length=32, default="")

class Solution(models.Model):
    title = models.CharField(max_length=256, default="")
    nickname = models.CharField(max_length=50, blank=True)
    points = models.BigIntegerField(default=0)