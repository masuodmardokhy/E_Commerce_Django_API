from django.db import models
from django.utils.timezone import datetime
from users .models import *
from product .models import *
from shopping_cart .models import *




class Cart_Item(models.Model):
    users = models.ForeignKey(Users, on_delete=models.CASCADE )
    product = models.OneToOneRel(Product, on_delete=models.CASCADE )
    shopping_cart = models.ForeignKey(Shapping_cart, on_delete=models.CASCADE )
    name = models.CharField(max_length=40)
    amount = models.PositiveIntegerField()
    price = models.PositiveIntegerField()

    # def __str__(self):
    #     return self.name
