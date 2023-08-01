from django.db import models
from core.models.base import *
from core.models.users import *
from core.models.product import *
from core.models.order import *
from core.models.shopping_cart import *


class Cart_Item(BaseModel):
    user = models.ForeignKey(Users, related_name='user_cartitem', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='product_cartitem', on_delete=models.CASCADE)
    order = models.ForeignKey(Order, related_name='order_cartitem', on_delete=models.CASCADE, null=True, blank=True)
    shopping_cart = models.ForeignKey(Shopping_Cart, related_name='shoppingcart_cartitem', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=40)
    amount = models.PositiveIntegerField(default=1)
    price = models.PositiveIntegerField()
    cart_image = models.ImageField(upload_to='cart_item_media', null= True)



    def __str__(self):
        return f"CartItem - ID: {self.id} - Shopping Cart: {self.shopping_cart}"

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



