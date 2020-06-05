from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import pre_save
from django.shortcuts import reverse
from django.utils.text import slugify

# Create your models here.


class Member(models.Model):
    id = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=50, verbose_name='Name')
    LastName = models.CharField(max_length=50, verbose_name='Last Name')
    email = models.EmailField(max_length=50, verbose_name="E-mail")
    printer_owner = models.BooleanField("")


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
