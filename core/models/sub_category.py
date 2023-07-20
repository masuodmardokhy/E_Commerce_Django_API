# from django.db import models
# from django.utils.timezone import datetime
# from core.models.base import *
# from core.models.category import *
#
#
#
# class Sub_Category(BaseModel):
#     # category = models.ForeignKey(Category, on_delete= models.CASCADE, default='')
#     name = models.CharField(max_length=30, default='')
#     slug = models.SlugField(allow_unicode=True, unique=True, null=True, blank=True)
#     image = models.ImageField(upload_to='sub_category_media')
#
#     def __str__(self):
#         return self.name
