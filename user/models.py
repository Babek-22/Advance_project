from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
   bio=models.TextField(max_length=500,blank=True,null=True)
   