from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class info(models.Model):
    g=(('MALE',"MALE"),('FEMALE','FEMALE'))
    name=models.CharField(max_length=30)
    gender=models.CharField(max_length=6,choices=g)
    dob=models.CharField(max_length=6)
    branch=models.CharField(max_length=30)
    phone=models.CharField(max_length=10)
    email=models.EmailField(max_length=50)


class ieeeUser(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    nickname=models.CharField(max_length=30,null=False)
def __str__(self):
    return self.nickname
