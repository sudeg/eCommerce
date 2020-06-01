from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import pre_save
from django.shortcuts import reverse
from django.utils.text import slugify

User = get_user_model()

class Address(models.Model):
    ADDRESS_CHOICES = (('B', 'Billing'),('S', 'Shipping'),)
    address_line_1 = models.CharField(max_length=150, null=True)
    address_line_2 = models.CharField(max_length=150, null=True)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    address_type = models.CharField(max_length=1, choices=ADDRESS_CHOICES, null=True)
    process_date = models.DateTimeField(auto_now_add=True) 
    default = models.BooleanField(default=False)

class ColourVariation(models.Model):
    name = models.CharField(max_length=50)

class SizeVariation(models.Model):
    name = models.CharField(max_length=50)

class DesignVariation(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='design_types', null=True)

class Product(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='product_images')
    description = models.TextField()
    price = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)
    available_colours = models.ManyToManyField(ColourVariation)
    available_sizes = models.ManyToManyField(SizeVariation)

class OrderItem(models.Model):
    order = models.ForeignKey("Order", related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    colour = models.ForeignKey(ColourVariation, on_delete=models.CASCADE, null=True)
    size = models.ForeignKey(SizeVariation, on_delete=models.CASCADE, null=True)

class Order(models.Model):
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField(blank=True, null=True)
    ordered = models.BooleanField(default=False)
    billing_address = models.ForeignKey(Address, related_name='billing_address', blank=True, null=True, on_delete=models.SET_NULL)
    shipping_address = models.ForeignKey(Address, related_name='shipping_address', blank=True, null=True, on_delete=models.SET_NULL)

class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='payments')
    payment_method = models.CharField(max_length=20, choices=(('PayPal', 'PayPal'),))
    timestamp = models.DateTimeField(auto_now_add=True)
    successful = models.BooleanField(default=False)
    amount = models.FloatField()
    raw_response = models.TextField()

class ThreeDimensionalDesign(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    imageOne = models.ImageField(upload_to='product_images', null=True)
    imageTwo = models.ImageField(upload_to='product_images', null=True)
    imageThree = models.ImageField(upload_to='product_images', null=True)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)
    available_colours = models.ManyToManyField(ColourVariation)
    available_sizes = models.ManyToManyField(SizeVariation)
    relatedType = models.ManyToManyField(DesignVariation)
    typeName = models.CharField(max_length=150, null=True)
