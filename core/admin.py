from django.contrib import admin
from .models import *
from django.template import loader
from django.utils.html import format_html
from django.shortcuts import render, redirect
from django.urls import reverse, path
from django.http import HttpResponse
from django import forms
import sys
import json
import requests
import urllib
import csv
import io


admin.site.register(Designer)
admin.site.register(DimensionalPrinter)
admin.site.register(PersonalInfo)


@admin.register(Printer)
class PrintersAdmin(admin.ModelAdmin):
    list_display = ['brand', 'modelName', 'created', 'updated']
    list_filter = ['updated']
    search_fields = ['brand', 'modelName']
    list_per_page = (20)
