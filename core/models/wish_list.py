from django.db import models
from core.models.base import *
from core.models.users import *
from core.models.product import *


class Wish_List(BaseModel):
    users = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='users_wishlist')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_wishlist')
    wishDate = models.DateTimeField(null=True, default=None)

    def __str__(self):
        return f"Wish ID: {self.id}, User: {self.users}, Product: {self.product}"