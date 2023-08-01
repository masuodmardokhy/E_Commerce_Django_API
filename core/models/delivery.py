from django.db import models
from core.models.base import *
from core.models.order import *
from core.models.shopping_cart import Shopping_Cart
from core.models.users import *

class Delivery(BaseModel):
    users = models.ForeignKey(Users,related_name='users_delivery', on_delete=models.CASCADE, null=True, blank=True)
    shopping_cart = models.OneToOneField(Shopping_Cart,related_name='shoppingcart_delivery', on_delete=models.CASCADE, null=True, blank=True)
    send_with = models.CharField(max_length=20)
    send_price = models.IntegerField(default=0)






