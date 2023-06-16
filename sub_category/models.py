from django.db import models
from django.utils.timezone import datetime
# from category.models import *
from base.models import *



class Sub_Category(BaseModel):
    #category = models.ForeignKey(Category, on_delete= models.CASCADE)
    name = models.CharField(max_length=30, null=True, blank=True)
    slug = models.SlugField(allow_unicode=True, unique=True, null=True, blank=True)
    image = models.ImageField(upload_to='gallery/sub_category')

    def __str__(self):
        return self.name
