from django.db import models
from django.utils.timezone import datetime
from base.models import *





class Category(BaseModel):
    name = models.CharField(max_length=50 )
    slug = models.SlugField(allow_unicode=True, unique=True, null=True, blank=True)
    image = models.ImageField(upload_to='gallery/category')

    def __str__(self):
        return self.name