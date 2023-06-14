from django.db import models
from django.utils.timezone import datetime
from product .models import *
from shopping_cart .models import *




class Order(models.Model):
    shopping_cart = models.OneToOneRel(Shapping_cart, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    quantity = models.PositiveIntegerField(default=1)
    price = models.PositiveIntegerField()
    address = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    date = models.DateField(default=datetime.today)
    status = models.BooleanField(default=False)

    def placeOrder(self):
        self.save()