from django.db import models
from django.utils.timezone import datetime
from category.models import *


# Base model built in Category model
class Sub_Category(BaseModel.Model):
    category = models.ForeignKey(Category, on_delete= models.CASCADE)
    slug = models.SlugField(allow_unicode=True, unique=True, null=True, blank=True)
    image = models.ImageField(upload_to='gallery/sub_category')

    def __str__(self):
        return self.name
