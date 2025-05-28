"""
SUPER SUER

USERNAME:socialmedia
PASSWORD:socialsocial

whenever a model is created , register it in the admin.urls page and
apply migrations
"""

from django.db import models
from django.conf import settings


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    photo = models.ImageField(upload_to ='users/%Y/%m%d',default='media/users/2024/0706/default-profile-photo.jpg')
    
    def __str__(self):
        return self.user.username