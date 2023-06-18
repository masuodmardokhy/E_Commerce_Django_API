from django.db import models
from base.models import *
from order.models import *


class Shopping_Cart(BaseModel):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, default='')
    total_price = models.PositiveIntegerField()
    total_amount = models.PositiveIntegerField()

    def __str__(self):
        return self.total_price
