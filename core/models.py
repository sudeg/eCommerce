from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import pre_save
from django.shortcuts import reverse
from django.utils.text import slugify

# Create your models here.
User = get_user_model()


class Designer(models.Model):
    brand = models.CharField(max_length=150)
    slug = models.SlugField()
    image = models.ImageField(
        upload_to='product_images', null=True, default=True)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    email = models.EmailField(max_length=150, default=True, null=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, default=True, null=True)
    countDesignerPros = models.IntegerField(default=True, null=True)

    def __str__(self):
        return self.brand


def pre_save_designer_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.brand)


pre_save.connect(pre_save_designer_receiver, sender=Designer)


class PrinterOwner(models.Model):
    brand = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    image = models.ImageField(
        upload_to='product_images', null=True, default=True)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, default=True, null=True)

    def __str__(self):
        return self.brand


def pre_save_PrinterOwner_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.brand)


pre_save.connect(pre_save_PrinterOwner_receiver, sender=PrinterOwner)


class DimensionalPrinter(models.Model):
    title = models.CharField(max_length=150)
    brand = models.CharField(max_length=150)
    image = models.ImageField(
        upload_to='product_images', null=True, default=True)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    price = models.IntegerField(default=0)
    email = models.EmailField(max_length=150, default=True, null=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.brand

    def get_price(self):
        return "{:.2f}".format(self.price / 100)

    def get_update_url(self):
        return reverse("core:dimensionalPrinters-update", kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse("core:dimensionalPrinters-delete", kwargs={'pk': self.pk})


class PersonalInfo(models.Model):
    age = models.IntegerField(default=0)
    image = models.ImageField(
        upload_to='product_images', null=True, default=True)
    info = models.TextField(null=True, default=True)
    fullName = models.TextField(null=True, default=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True)
    email = models.EmailField(max_length=150, default=True, null=True)

    def __str__(self):
        return self.fullName


# TUNA BU YENI OLUSTURDUGUM PRINTER USTTEKILER MERGE'E DUSUCEK BU COMMENT ASAGISINI TUT TAMAM MI

class Printer(models.Model):
    brand = models.CharField(max_length=150)
    modelName = models.CharField(max_length=250)
    imageOne = models.ImageField(
        upload_to='printer_images', null=True, default=True)
    imageTwo = models.ImageField(
        upload_to='printer_images', null=True, default=True)
    imageThree = models.ImageField(
        upload_to='printer_images', null=True, default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s %s' % (self.brand, self.modelName)
