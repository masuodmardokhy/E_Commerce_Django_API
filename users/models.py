from django.db import models
from product.models import *
from cart_item.models import *
from django.utils.timezone import datetime







class Users(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE )
    cart_list = models.ForeignKey(Cart_List, on_delete=models.CASCADE )
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    password = models.CharField(max_length=60)

    def register(self):
        self.save()

    @staticmethod
    def user_by_email(getemail):
        try:
            return Users.objects.get(email=getemail)
        except:
            return False

    def isExists(self):
        if Users.objects.filter(email=self.email):
            return True
        else:
            return False
