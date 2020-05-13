from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import pre_save
from django.shortcuts import reverse
from django.utils.text import slugify

# Create your models here.
User = get_user_model()


class Designer(models.Model):
    brand = models.CharField(max_length=150)
    image = models.ImageField(
        upload_to='product_images', null=True, default=True)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, default=True, null=True)

    def __str__(self):
        return self.brand

    # def get_absolute_url(self):
    #     return reverse("cart:product-detail", kwargs={'slug': self.slug})

    # def get_update_url(self):
    #     return reverse("staff:product-update", kwargs={'pk': self.pk})

    # def get_delete_url(self):
    #     return reverse("staff:product-delete", kwargs={'pk': self.pk})

    # def get_price(self):
    #     return "{:.2f}".format(self.price / 100)
