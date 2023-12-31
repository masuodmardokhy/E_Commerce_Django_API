from django.db import models
from django.utils.timezone import datetime
from core.models.base import *
from django.utils.text import slugify
from core.models.users import *
import re   # Regular Expression to be tidy slug




class Category(BaseModel):
    users = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='users_category')
    name = models.CharField(max_length=50)
    slug = models.SlugField(allow_unicode=True, null=True, blank=True)
    image = models.ImageField(upload_to='category_media', null=True, blank=True)
    sub = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subcategories')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = persian_slugify(self.name)
        super().save(*args, **kwargs)


def persian_slugify(value):   # for create slug field with persian language
    value = re.sub(r'(a(?!([eiou]|$)))|e|i|o|u', '', value, flags=re.IGNORECASE)     # Remove extra words from the name
    return slugify(value, allow_unicode=True)    # Convert name to slug

