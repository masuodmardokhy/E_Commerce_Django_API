from django.db import models
from base.models import *
from shopping_cart .models import *


class Delivery(BaseModel):
    shopping_cart = models.OneToOneField(Shopping_Cart, on_delete=models.CASCADE, default='')
    send_with_post = models.BooleanField(default=False)
    products_price = models.PositiveIntegerField()
    send_price = models.PositiveIntegerField()
    total_cost = models.PositiveIntegerField()

    @property
    def total_cost(self):
        if self.send_with_post is True:
            return int (self.products_price + self.send_price)
        else:
            return self.products_price




