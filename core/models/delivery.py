from django.db import models
from core.models.base import *
from core.models.shopping_cart import *




class Delivery(BaseModel):
    shopping_cart = models.OneToOneField(Shopping_Cart, on_delete=models.CASCADE, default='')
    total_amount_product= models.PositiveIntegerField(default=0)
    send_to_out_Capital = models.BooleanField(default=False)
    send_price = models.PositiveIntegerField(default=10)
    total_price = models.PositiveIntegerField()

    @property
    def calculate_total_price(self):
        if self.send_to_out_Capital:
            return self.total_price + self.send_price
        return self.total_price




