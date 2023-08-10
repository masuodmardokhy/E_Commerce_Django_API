from django.db import models
from django.utils.timezone import datetime
from django.core.validators import MinLengthValidator
from core.models.base import *
from core.models.users import *
from core.models.delivery import Delivery
from core.models.address import *
from django.utils.timezone import now
from core.models.shopping_cart import Shopping_Cart


class Order(BaseModel):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='user_order')
    address = models.OneToOneField('Address', on_delete=models.CASCADE, related_name='address_order')
    shopping_cart = models.ForeignKey(Shopping_Cart, on_delete=models.CASCADE, related_name='shoppingcart_order')
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE, related_name='delivery_order')
    total_price = models.PositiveIntegerField()
    send_price = models.PositiveIntegerField(default=0)
    total_price_with_send_price = models.PositiveIntegerField(default=0)
    order_date = models.DateTimeField(default=now)


    def __str__(self):
        return f"Order ID: {self.id}, User: {self.user}, Order Date: {self.order_date}"
