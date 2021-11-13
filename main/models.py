from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Task(models.Model):
    title=models.CharField(max_length=400,null=True,blank=True)
    created=models.DateTimeField(null=True,blank=True)
    assigned=models.ForeignKey(settings.AUTH_USER_MODEL,null=True,blank=True,on_delete=models.SET_NULL)
    description=models.TextField(null=True,blank=True)
    status=models.CharField(max_length=300,null=True,blank=True)
    is_completed=models.BooleanField(default=False)
