from django.db import models
from django.utils.timezone import datetime
from base.models import *
from users.models import *
from sub_category.models import *


class Product(BaseModel):
    users = models.ForeignKey(Users, on_delete=models.CASCADE, default=1)
    sub_category = models.ForeignKey(Sub_Category, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=30)
    slug = models.SlugField(allow_unicode=True, unique=True, null=True, blank=True)
    amount = models.PositiveIntegerField()
    unit_price = models.PositiveIntegerField()
    discount = models.PositiveIntegerField(blank=True, null=True)
    total_price = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    description = models.CharField(max_length=300, blank=True, null=True)
    image = models.ImageField(upload_to='product_media', null= True)

    def __str__(self):
        return self.name


    @staticmethod
    def products_by_id(id):
        return Product.objects.filter(category_id=id)

    @property
    def total_price(self):         #we have this function to discount products.
        if not self.discount:           #If there is a discount, calculate it and show the result in the total_price
            return self.unit_price
        elif self.discount:
            t = (self.unit_price * self.discount)/100
            return int(self.unit_price - t)
        return self.total_price


    # @property
    # def image_display(self):
    #     if self.image:
    #         return self.image.url
    #     return None