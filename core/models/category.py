from django.db import models
from django.utils.timezone import datetime
from core.models.base import *





class Category(BaseModel):
    name = models.CharField(max_length=50)
    slug = models.SlugField(allow_unicode=True, unique=True, null=True, blank=True)
    image = models.ImageField(upload_to='category_media')
    sub = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subcategories')

    def __str__(self):
        return self.name
