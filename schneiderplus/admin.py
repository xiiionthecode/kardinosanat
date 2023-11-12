from django.contrib import admin
from .models import *

class SliderAdmin(admin.ModelAdmin):
    list_display = ['title', 'active']
admin.site.register(Slider, SliderAdmin)

class SupportAdmin(admin.ModelAdmin):
    list_display = ['tel_phone_1th']
admin.site.register(Support, SupportAdmin)
