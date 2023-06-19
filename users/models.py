from django.db import models
# from product .models import *
# from cart_item .models import *
from django.utils.timezone import datetime
from base.models import *
from django.core.validators import MinLengthValidator



class Users(BaseModel):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    phone = models.CharField(max_length=15,  validators=[MinLengthValidator(11)])
    password = models.CharField(max_length=60)

    def register(self):
        self.save()

    def __str__(self):
        return self.last_name

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
