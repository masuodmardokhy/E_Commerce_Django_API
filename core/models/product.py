from django.db import models
from django.utils.timezone import datetime
from core.models.base import *
from core.models.users import *
from core.models.category import *
from django.utils.text import slugify
import re
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit


#
# class ProductImage(models.Model):
#     product = models.ForeignKey('Product', related_name='product_productimage', on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='product_media', null=True)
#
#     def __str__(self):
#         return f"{self.product.name} - Image {self.id}"
#

# class ProductImage(models.Model):
#     image = models.ImageField(upload_to='product_media',blank=True, null=True)
#
#     def __str__(self):
#         return f"Product Image ID: {self.id}"


class Product(BaseModel):
    COLOR_CHOICES = (
        ('', '---'),
        ('white', 'white'),
        ('red', 'red'),
        ('blue', 'blue'),
        ('green', 'green'),
        ('yellow', 'yellow'),
        ('purple', 'purple'),
        ('orange', 'orange'),
        ('pink', 'pink'),
        ('brown', 'brown'),
        ('gray', 'gray'),
        ('black', 'black'),
    )
    SIZE_CHOICES = (
        ('', '---'),
        ('small', 'small'),
        ('medium', 'medium'),
        ('large', 'large'),
        ('Xـlarge', 'Xـlarge'),
    )

    users = models.ForeignKey(Users, on_delete=models.CASCADE, default=1, related_name='user_product')
    category = models.ForeignKey(Category, related_name='category_product', on_delete=models.CASCADE)

    name = models.CharField(max_length=30)
    slug = models.SlugField(allow_unicode=True, unique=True, null=True, blank=True)
    amount = models.PositiveIntegerField(default=1)
    unit_price = models.PositiveIntegerField()
    discount = models.PositiveIntegerField(blank=True, null=True)
    total_price = models.PositiveIntegerField(default=0)
    available = models.BooleanField(default=True)
    description = models.CharField(max_length=300, blank=True, null=True)
    images = models.JSONField(null=True, blank=True)
    color = models.CharField(max_length=30, choices=COLOR_CHOICES, blank=True, null=True, default=None)
    size = models.CharField(max_length=30, choices=SIZE_CHOICES, blank=True, null=True, default=None)


    def __str__(self):
        return self.name

    @property
    def calculate_total_price(self):   # Property to calculate the total price
        if not self.discount:
            return self.unit_price
        else:
            t = (self.unit_price * self.discount) / 100
            return int(self.unit_price - t)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = persian_slugify(self.name)
        super().save(*args, **kwargs)


def persian_slugify(value):   # for create slug field with persian language
    value = re.sub(r'(a(?!([eiou]|$)))|e|i|o|u', '', value, flags=re.IGNORECASE)     # Remove extra words from the name
    return slugify(value, allow_unicode=True)    # Convert name to slug


    # @staticmethod
    # def products_by_id(id):
    #     return Product.objects.filter(category_id=id)

    # @property
    # def image_display(self):
    #     if self.image:
    #         return self.image.url
    #     return None


