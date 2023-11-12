from django.contrib import admin
from .models import *

class BlogLogsAdmin(admin.ModelAdmin):
    list_display = ['id' , 'author' , 'status' , 'msg' , 'J_addition_datetime']
admin.site.register(BlogLogs , BlogLogsAdmin)

class BrandLogsAdmin(admin.ModelAdmin):
    list_display = ['id' , 'author' , 'status' , 'msg' , 'J_addition_datetime']
admin.site.register(BrandLogs , BrandLogsAdmin)

class CategorylogsAdmin(admin.ModelAdmin):
    list_display = ['id' , 'author' , 'status' , 'msg' , 'J_addition_datetime']
admin.site.register(Categorylogs , CategorylogsAdmin)