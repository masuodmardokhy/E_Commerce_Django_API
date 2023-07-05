from django.db import models
from django.utils.timezone import datetime
from django.core.validators import MinLengthValidator
from core.models.base import *







class Order(BaseModel):
    # shopping_cart = models.OneToOneRel(Shopping_Cart, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    quantity = models.PositiveIntegerField(default=1)
    price = models.PositiveIntegerField()
    address = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=15,  validators=[MinLengthValidator(11)])
    date = models.DateField(default=datetime.today)
    status = models.BooleanField(default=False)

    def placeOrder(self):
        self.save()

    def __str__(self):
        return self.name