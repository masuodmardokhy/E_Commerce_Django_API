from django.db import models
from core.models.base import *
from core.models.order import *
from core.models.users import *
from core.models.cart_item import *
from core.models.delivery import Delivery


class Shopping_Cart(BaseModel):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, default='')

    cart_items = models.JSONField(null=True, blank=True)



