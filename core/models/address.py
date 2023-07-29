from django.db import models
from core.models.base import *
from core.models.order import Order


class Address(BaseModel):
    order = models.OneToOneField(Order, related_name='address', on_delete=models.CASCADE)

    stat = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    zipCode = models.CharField(max_length=20)


    def __str__(self):
        return f"Address ID: {self.addressId}, City: {self.city}"