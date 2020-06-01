from django.contrib import admin
from .models import *

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['address_line_1','address_line_2','city','zip_code','address_type',]

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','description','price',]
    list_filter  = ['title']
    search_fields = ['title']

@admin.register(SizeVariation)
class SizeVariationAdmin(admin.ModelAdmin):
    list_display = ['name']
    
@admin.register(ColourVariation)
class ColourVariationAdmin(admin.ModelAdmin):
    list_display = ['name']
    
@admin.register(DesignVariation)
class DesignVariationAdmin(admin.ModelAdmin):
    list_display = ['name']
