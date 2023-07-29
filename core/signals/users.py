# from django.db.models.signals import pre_delete
# from django.dispatch import receiver
# from core.models.users import Users
#
#
#
#
#
# #When we delete a record that includes a photo in the database,
# # the corresponding photo in our project folder must also be deleted.  +     def ready(self):  import product.signals in the apps product
#
#
# @receiver(pre_delete, sender=Users)
# def delete_users_image(sender, instance, **kwargs):
#     # Check if the instance has an image
#     if instance.user_image:
#         # Delete the image file from the filesystem
#         instance.user_image.delete(save=False)