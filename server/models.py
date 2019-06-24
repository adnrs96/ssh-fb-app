from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.db import models

# Create your models here.
class UserProfile(AbstractBaseUser):
    USERNAME_FIELD = 'user_id'
    user_id = models.CharField(unique=True, max_length=32)
    access_token = models.CharField(max_length=200)
    is_active = models.BooleanField()
    objects = UserManager()
