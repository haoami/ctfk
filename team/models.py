from django.db import models

# Create your models here.
class Team(models.Model):
    team_leader = models.CharField(max_length=50,default="无")
    pub_date = models.DateTimeField(auto_now=True)
    team_name = models.CharField(max_length=50,unique=True)
    content = models.TextField(default="")
    logo = models.CharField(max_length=250)
    population=models.IntegerField(default=1)
    
class Relationship(models.Model):
    team_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)

