from django.db import models
from django.utils.timezone import datetime
from django.core.validators import MinLengthValidator
from core.models.base import *
from core.models.users import *


class Order(BaseModel):
    user = models.OneToOneField(Users, on_delete=models.CASCADE, default='')
    name = models.CharField(max_length=30)
    total_price = models.PositiveIntegerField()
    total_amount_product= models.PositiveIntegerField(default=0)
    address = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=15,  validators=[MinLengthValidator(11)])
    date = models.DateField(default=datetime.today)

    def __str__(self):
        return self.name