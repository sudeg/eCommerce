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


class Printers(models.Model):
    brand = models.CharField(max_length=150)
    slug = models.SlugField()
    image = models.ImageField(
        upload_to='product_images', null=True, default=True)
    description = models.TextField()
    # singleExtruderPrint= models.CharField(max_length=150)
    # dualExtruderPrint = models.CharField(max_length=150)
    # machineSize = models.CharField(max_length=150)
    # printTechnology = models.CharField(max_length=150)
    # printHeadSsytem = models.CharField(max_length=150)
    # filamentDiameter = models.CharField(max_length=150)
    # XYZStepSize = models.CharField(max_length=150)
    # printHeadTravelSpeed = models.CharField(max_length=150)
    # buildPlate = models.CharField(max_length=150)
    # plateTemperature = models.CharField(max_length=150)
    # bedMaterial = models.CharField(max_length=150)
    # layerHeight = models.CharField(max_length=150)
    # nozzleDiameter = models.CharField(max_length=150)
    # hotEnd = models.CharField(max_length=150)
    # maxNozzleTemperature = models.CharField(max_length=150)
    # connectivity = models.CharField(max_length=150)
    # noiseEmission = models.CharField(max_length=150)
    # ambientTemperature = models.CharField(max_length=150)
    # storageTemperature = models.CharField(max_length=150)
    # filters = models.CharField(max_length=150)


def pre_save_Printer_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.brand)


pre_save.connect(pre_save_Printer_receiver, sender=Printers)


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
