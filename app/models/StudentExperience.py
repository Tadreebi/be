from time import time
from django.contrib.auth import get_user_model
from django.db import models

class StudentExperience(models.Model):
    student = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    Company = models.CharField(max_length=64)
    time = models.DateTimeField(auto_now_add=True)
    recommend = models.BooleanField(null=True,blank=True)
    detail_experience= models.TextField(max_length=256,null=True,blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


