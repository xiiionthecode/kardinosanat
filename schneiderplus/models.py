from django.db import models
from django.utils.translation import gettext as _

def sliderPosterPath(instance, filename):
    name = instance.title.replace(' ','-')
    filename = filename.replace(' ','-')
    return 'schneiderplus/Images/{0}/{1}'.format(name,filename)

class Slider(models.Model):
    title = models.CharField(max_length=255)
    alt = models.CharField(max_length=255)
    picture = models.ImageField(upload_to=sliderPosterPath , null=True , blank=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField(default=True)

class Support(models.Model):
    tel_phone_1th = models.CharField(_('this number for call to you about buying product'), max_length=255, blank=True, null=True)
    tel_phone_2th = models.CharField(max_length=255, blank=True, null=True)
    mobile_phone_1th = models.CharField(max_length=255, blank=True, null=True)
    mobile_phone_2th = models.CharField(max_length=255, blank=True, null=True)
    telegram_phone = models.CharField(max_length=255, blank=True, null=True)
    whatsapp_phone = models.CharField(max_length=255, blank=True, null=True)
    ita_phone = models.CharField(max_length=255, blank=True, null=True)
    rubika_phone = models.CharField(max_length=255, blank=True, null=True)
    instagram_id = models.CharField(max_length=255, blank=True, null=True)
    telegram_id = models.CharField(max_length=255, blank=True, null=True)
    address_1th = models.CharField(max_length=255, blank=True, null=True)
    address_2th = models.CharField(max_length=255, blank=True, null=True)
    mail = models.CharField(max_length=255, blank=True, null=True)
    week = models.CharField(_('Working hours on weeks'), max_length=255, blank=True, null=True)
    weekend = models.CharField(_('Working hours on weekends'), max_length=255, blank=True, null=True)