from django.contrib import admin
from .models import *


@admin.register(Printer)
class PrintersAdmin(admin.ModelAdmin):
    list_display = ['brand', 'modelName', 'created', 'updated']
    list_filter = ['updated']
    search_fields = ['brand', 'modelName']
    list_per_page = (20)
