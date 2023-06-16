from django.db import models
from base.models import *
from django.utils.timezone import datetime
# from product .models import *
# from shopping_cart .models import *
#from users .models import Users



class Cart_Item(BaseModel):
    #users = models.ForeignKey(Users, on_delete=models.CASCADE )
    #product = models.OneToOneRel(Product, on_delete=models.CASCADE)
    #shopping_cart = models.ForeignKey(Shopping_Cart, on_delete=models.CASCADE )
    name = models.CharField(max_length=40)
    amount = models.PositiveIntegerField()
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.name
