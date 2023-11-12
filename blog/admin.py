from django.contrib import admin
from .models import *

class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'title', 'active']
admin.site.register(Blog, BlogAdmin)

class BlogTagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'numberOfUsed', 'numbOfClicked', 'active']
admin.site.register(BlogTag, BlogTagAdmin)

