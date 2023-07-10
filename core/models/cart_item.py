from django.db import models
from core.models.base import *
from core.models.users import *
from core.models.product import *
from core.models.shopping_cart import *


class Cart_Item(BaseModel):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, default='')
    product = models.OneToOneField(Product, on_delete=models.CASCADE, default='')
    shopping_cart = models.ForeignKey(Shopping_Cart, on_delete=models.CASCADE, default='', null=True)
    name = models.CharField(max_length=40)
    amount = models.PositiveIntegerField()
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    @classmethod
    def create_from_product(cls, product, user, shopping_cart):
        cart_item = cls(
            user=user,
            product=product,
            shopping_cart=shopping_cart,
            name=product.name,
            amount=product.amount,
            price=product.get_total_price()
        )
        cart_item.save()
        return cart_item
