from django.contrib import admin
from .models import *

class FeaturesCategoriesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'active']
admin.site.register(FeaturesCategories, FeaturesCategoriesAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'Brand', 'ProductCategorySubset', 'faName', 'code', 'view', 'active']
admin.site.register(Product, ProductAdmin)

class FeatureAdmin(admin.ModelAdmin):
    list_display = ['id', 'Product', 'FeaturesCategories', 'feature', 'descriptions', 'important', 'active']
admin.site.register(Feature, FeatureAdmin)

class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'Product', 'enName', 'image', 'active']
admin.site.register(ProductImage, ProductImageAdmin)

class ProductTagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'numberOfUsed', 'numbOfClicked', 'active']
admin.site.register(ProductTag, ProductTagAdmin)