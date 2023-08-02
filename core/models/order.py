from django.db import models
from django.utils.timezone import datetime
from django.core.validators import MinLengthValidator
from core.models.base import *
from core.models.users import *
from core.models.delivery import *
from core.models.address import *

class Order(BaseModel):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='user_order')
    delivery = models.OneToOneField(Delivery,  related_name='delivery_order', on_delete=models.CASCADE)
    address = models.OneToOneField(Address, related_name='address_order', on_delete=models.CASCADE)

    name = models.CharField(max_length=30)
    total_price = models.PositiveIntegerField()
    total_amount_product= models.PositiveIntegerField(default=0)
    phone = models.CharField(max_length=15,  validators=[MinLengthValidator(11)])
    date = models.DateField(default=datetime.today)

    def __str__(self):
        return f"Order ID: {self.Id}, Product: {self.name}"