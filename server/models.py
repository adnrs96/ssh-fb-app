from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.db import models
from django.core.files import File
import urllib
import os

# Create your models here.
class UserProfile(AbstractBaseUser):
    USERNAME_FIELD = 'user_id'
    user_id = models.CharField(unique=True, max_length=32)
    full_name = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='profile_pics')
    access_token = models.CharField(max_length=200)
    is_active = models.BooleanField()
    objects = UserManager()

    def update_profile_picture_from_url(self, url):
        """Store image locally if we have a URL"""
        result = urllib.request.urlretrieve(url)
        self.profile_picture.save(
            os.path.basename(url),
            File(open(result[0], 'rb'))
        )
