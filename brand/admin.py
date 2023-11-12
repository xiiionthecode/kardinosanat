from django.contrib import admin
from .models import *

class Brandadmin(admin.ModelAdmin):
    list_display = ['id', 'en_name', 'number_of_products', 'active']
admin.site.register(Brand, Brandadmin)
