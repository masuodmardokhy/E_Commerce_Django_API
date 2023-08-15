from django.contrib.auth.models import User
from django.db import models
from django.conf import settings


# class Token(models.Model):
#     user = models.OneToOneField(User,settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     token = models.CharField(max_length=255)
