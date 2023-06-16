from django.db import models
from base.models import *


class Shopping_Cart(BaseModel):
    total_price = models.PositiveIntegerField()
    total_amount = models.PositiveIntegerField()

    def __str__(self):
        return self.total_price
