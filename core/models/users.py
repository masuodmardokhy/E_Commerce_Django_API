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
            active=True
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
    last_login = models.DateTimeField(null=True, blank=True)  # The last login time of the user must be shown in this field
    active = models.BooleanField(default=True)  # If the user deletes her account, the active field in the database should be false
    is_admin = models.BooleanField(default=False)
    create = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update = models.DateTimeField(auto_now=True, null=True)
    user_image = models.ImageField(upload_to='user_image_media', null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name', 'last_name', 'phone','password']

    objects = UserManager()

    def __str__(self):
        return self.user_name

    # def get_full_name(self):
    #     return f"{self.first_name} {self.last_name}"
    #
    # def get_short_name(self):
    #     return self.first_name
    #
    # def has_perm(self, perm, obj=None):
    #     return True
    #
    # def has_module_perms(self, app_label):
    #     return True
    #
    # @property
    # def is_staff(self):
    #     return self.is_admin

    def register(self):
        self.save()



