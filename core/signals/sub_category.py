from django.db.models.signals import pre_delete
from django.dispatch import receiver
from core.models.product import Product






#When we delete a record that includes a photo in the database,
# the corresponding photo in our project folder must also be deleted.  +     def ready(self):  import product.signals in the apps product


@receiver(pre_delete, sender=Product)
def delete_product_image(sender, instance, **kwargs):
    # Check if the instance has an image
    if instance.image:
        # Delete the image file from the filesystem
        instance.image.delete(save=False)