from django.db import models
from core.models.base import *
from core.models.order import *
from core.models.users import *
from core.models.cart_item import *


class Shopping_Cart(BaseModel):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, default='')
    cart_items = models.JSONField(default=list)
    total_price = models.PositiveIntegerField(default=0)
    total_amount_item = models.PositiveIntegerField(default=0)
    total_amount_product = models.PositiveIntegerField(default=0)








    # cart_items = models.JSONField(null=True, blank=True)



