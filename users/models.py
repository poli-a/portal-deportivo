from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


    
class User(AbstractUser):
    username = models.CharField(max_length = 30, unique=True)
    is_active = models.BooleanField(default=True)
    USERNAME_FIELD = 'username'
    is_admin = models.BooleanField(default = False)