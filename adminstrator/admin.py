from django.contrib import admin
from .models import AdminLogin , AdminInfo

class AdminLoginAdmin(admin.ModelAdmin):
    list_display = ['id' , 'username' , 'mail' , 'joined_at' , 'lastlogin']
admin.site.register(AdminLogin , AdminLoginAdmin)

class AdminInfoAdmin(admin.ModelAdmin):
    list_display = ['id' , 'firstname' , 'lastname' , 'AdminLogin' , 'complited_at']
admin.site.register(AdminInfo , AdminInfoAdmin)