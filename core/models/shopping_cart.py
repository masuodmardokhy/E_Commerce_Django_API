from django.db import models
from core.models.base import *
from core.models.order import *
from core.models.users import *
from core.models.cart_item import *
from core.models.delivery import Delivery


class Shopping_Cart(BaseModel):
    BOOLEAN_CHOICES = [
        (False, 'send_with_post'),
        (False, 'send_with_tipax'),
        (False, 'send_with_snapbar'),
    ]
    delivery = models.BooleanField(choices=BOOLEAN_CHOICES)

    user = models.ForeignKey(Users, on_delete=models.CASCADE, default='')
    delivery_id = models.OneToOneField(Delivery, on_delete=models.SET_NULL, null=True)
    total_amount_item = models.PositiveIntegerField()
    total_amount_product = models.PositiveIntegerField(default=0)
    total_price = models.PositiveIntegerField()

    @property
    def calculated_total_price(self):
        if self.delivery:
            return self.total_price + self.delivery_id.send_with_post + self.delivery_id.send_with_tipax + self.delivery_id.send_with_snapbar
        return self.total_price