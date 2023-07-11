from django.db import models
from core.models.base import *
from core.models.order import *
from core.models.users import *
from core.models.cart_item import *


class Shopping_Cart(BaseModel):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, default='')
    user = models.OneToOneField(Users, on_delete=models.CASCADE, default='')
    total_price = models.PositiveIntegerField()
    total_amount = models.PositiveIntegerField()

    def __str__(self):
        return self.total_price
