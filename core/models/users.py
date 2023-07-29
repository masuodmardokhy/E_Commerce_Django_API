from django.db import models
from django.utils.timezone import datetime
from django.core.validators import MinLengthValidator
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from core.models.base import *
from django.db.models.signals import pre_delete
from core.signals.users import *




class Users(BaseModel):
    user_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    phone = models.CharField(max_length=15,  validators=[MinLengthValidator(11)])
    password = models.CharField(max_length=100)
    last_login = models.DateTimeField(null=True, blank=True)
    active = models.BooleanField(default=True)
    # rest_token = models.TextField()
    user_image = models.ImageField(upload_to='user_image_media', null= True)


    def register(self):
        self.save()

    def __str__(self):
        return self.user_name

    @staticmethod
    def user_by_email(getemail):
        try:
            return Users.objects.get(email=getemail)
        except:
            return False

    @staticmethod
    def isExists(self):
        if Users.objects.filter(email=self.email):
            return True
        else:
            return False



# pre_delete.connect(delete_users_image, sender=Users)     # for delete images after remove user








# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, phone, password=None, **extra_fields):
#         if not email:
#             raise ValueError('The Email field must be set')
#         if not phone:
#             raise ValueError('The Phone field must be set')
#
#         email = self.normalize_email(email)
#         user = self.model(email=email, phone=phone, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, email, phone, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         return self.create_user(email, phone, password, **extra_fields)
#
#
# class Users(AbstractBaseUser):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=40)
#     email = models.EmailField(unique=True)
#     phone = models.CharField(max_length=15, unique=True, validators=[MinLengthValidator(11)])
#     password = models.CharField(max_length=60)
#     create = models.DateTimeField(auto_now_add=True, null=True, blank=True)
#     update = models.DateTimeField(auto_now=True, null=True)
#
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['phone']
#
#     objects = CustomUserManager()
#
#     def __str__(self):
#         return self.email
