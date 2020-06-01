from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import pre_save
from django.shortcuts import reverse
from django.utils.text import slugify

# Create your models here.
User = get_user_model()

class DimensionalPrinter(models.Model):
    title = models.CharField(max_length=150)
    brand = models.CharField(max_length=150)
    image = models.ImageField(upload_to='product_images', null=True, default=True)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    price = models.IntegerField(default=0)
    email = models.EmailField(max_length=150, default=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

class PersonalInfo(models.Model):
    age = models.IntegerField(default=0)
    image = models.ImageField(upload_to='product_images', null=True, default=True)
    info = models.TextField(null=True, default=True)
    fullName = models.TextField(null=True, default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    email = models.EmailField(max_length=150, default=True, null=True)

    def __str__(self):
        return self.fullName
