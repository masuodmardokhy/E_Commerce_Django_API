from django.db import models
from core.models.base import *
from core.models.users import *
from core.models.product import *
from core.models.shopping_cart import *





class Cart_Item(BaseModel):
    users = models.ForeignKey(Users, on_delete=models.CASCADE , default='')
    product = models.OneToOneField(Product, on_delete=models.CASCADE, default='')
    shopping_cart = models.ForeignKey(Shopping_Cart, on_delete=models.CASCADE, default='' )
    name = models.CharField(max_length=40)
    amount = models.PositiveIntegerField()
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.name
