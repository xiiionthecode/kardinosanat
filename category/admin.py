from django.contrib import admin
from .models import *

class ProductCategoryadmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'number_of_products', 'active']
admin.site.register(ProductCategory, ProductCategoryadmin)

class ProductCategorySubsetadmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'subset_number', 'number_of_products', 'active']
admin.site.register(ProductCategorySubset, ProductCategorySubsetadmin)
