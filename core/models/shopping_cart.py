from django.db import models
from core.models.base import *
from core.models.order import *


class Shopping_Cart(BaseModel):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, default='')
    total_price = models.PositiveIntegerField()
    total_amount = models.PositiveIntegerField()

    def __str__(self):
        return self.total_price
