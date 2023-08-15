from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone

class UserManager(BaseUserManager):
    def create_user(self, email, user_name, first_name, last_name, phone, password=None):
        if not email:
            raise ValueError('The Email field must be set')
        user = self.model(
            email=self.normalize_email(email),
            user_name=user_name,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, user_name, first_name, last_name, phone, password=None):
        user = self.create_user(
            email=email,
            user_name=user_name,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            password=password,
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Users(AbstractBaseUser):
    user_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, validators=[MinLengthValidator(11)])
    password = models.CharField(max_length=100)
    last_login = models.DateTimeField(null=True, blank=True)
    active = models.BooleanField(default=True)
    create = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update = models.DateTimeField(auto_now=True, null=True)
    user_image = models.ImageField(upload_to='user_image_media', null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name', 'last_name', 'phone']

    objects = UserManager()

    def __str__(self):
        return self.user_name

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self):
        return self.first_name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    def register(self):
        self.save()




# from django.db import models
# from django.utils.timezone import datetime
# from django.core.validators import MinLengthValidator
# from rest_framework.authtoken.models import Token
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# from core.models.base import *
# from django.db.models.signals import pre_delete
# from core.signals.users import *
#
#
#
# class UserManager(BaseUserManager):
#     def create_user(self, email, first_name, last_name, phone, create, password):
#         user = self.model(email=self.normalize_email(email), first_name=first_name, last_name=last_name, phone=phone,
#                           create=create, )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, email, first_name, last_name, phone, create, password):
#         user = self.create_user(email, first_name, last_name, phone, create, password)
#         user.is_admin = True
#         user.is_superuser = True
#         user.save(using=self._db)
#         return user
#
#     def get_by_natural_key(self, email):
#         return self.get(email=email)
#
#
# class Users(AbstractBaseUser):
#     # user_name = models.CharField(max_length=30)
#     # first_name = models.CharField(max_length=30)
#     # last_name = models.CharField(max_length=40)
#     # email = models.EmailField(unique=True)
#     # phone = models.CharField(max_length=15,  validators=[MinLengthValidator(11)])
#     # password = models.CharField(max_length=100)
#     # last_login = models.DateTimeField(null=True, blank=True)
#     # active = models.BooleanField(default=True)
#     # # rest_token = models.TextField()
#     # user_image = models.ImageField(upload_to='user_image_media', null= True)
#
#     # USERNAME_FIELD = 'email'
#     # # REQUIRED_FIELDS = ['email',]
#     #
#     # objects = UserManager()
#     #
#     # def register(self):
#     #     self.save()
#     #
#     # def __str__(self):
#     #     return self.user_name
#     #
#     # @staticmethod
#     # def user_by_email(getemail):
#     #     try:
#     #         return Users.objects.get(email=getemail)
#     #     except:
#     #         return False
#     #
#     # @staticmethod
#     # def isExists(self):
#     #     if Users.objects.filter(email=self.email):
#     #         return True
#     #     else:
#     #         return False
#     #
#
#
# # pre_delete.connect(delete_users_image, sender=Users)     # for delete images after remove user
#
#
#
#
#
#
#
#
# # class CustomUserManager(BaseUserManager):
# #     def create_user(self, email, phone, password=None, **extra_fields):
# #         if not email:
# #             raise ValueError('The Email field must be set')
# #         if not phone:
# #             raise ValueError('The Phone field must be set')
# #
# #         email = self.normalize_email(email)
# #         user = self.model(email=email, phone=phone, **extra_fields)
# #         user.set_password(password)
# #         user.save(using=self._db)
# #         return user
# #
# #     def create_superuser(self, email, phone, password=None, **extra_fields):
# #         extra_fields.setdefault('is_staff', True)
# #         extra_fields.setdefault('is_superuser', True)
# #         return self.create_user(email, phone, password, **extra_fields)
# #
# #
# # class Users(AbstractBaseUser):
# #     first_name = models.CharField(max_length=30)
# #     last_name = models.CharField(max_length=40)
# #     email = models.EmailField(unique=True)
# #     phone = models.CharField(max_length=15, unique=True, validators=[MinLengthValidator(11)])
# #     password = models.CharField(max_length=60)
# #     create = models.DateTimeField(auto_now_add=True, null=True, blank=True)
# #     update = models.DateTimeField(auto_now=True, null=True)
# #
# #     is_active = models.BooleanField(default=True)
# #     is_staff = models.BooleanField(default=False)
# #
# #     USERNAME_FIELD = 'email'
# #     REQUIRED_FIELDS = ['phone']
# #
# #     objects = CustomUserManager()
# #
# #     def __str__(self):
# #         return self.email
