from django.db import models
from django.utils.timezone import datetime


class BaseModel(models.Model):
    name = models.CharField(max_length=50)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(BaseModel.Model):
    slug = models.SlugField(allow_unicode=True, unique=True, null=True, blank=True)
    image = models.ImageField(upload_to='gallery/category')

    def __str__(self):
        return self.name