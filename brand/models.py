from django.db import models
from django.utils.translation import gettext as _
import uuid, os 
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

def BrandLogoImagePath(instance, filename):
    
    if ' ' in instance.en_name:
        name = instance.en_name.replace(' ','-')
        filename = filename.replace(' ','-')
    if '_' in instance.en_name:
        name = instance.en_name.replace('_','-')
        filename = filename.replace('_','-')
    else:
        name = instance.en_name
        filename = filename

    return 'Brands/Images/{0}/{1}'.format(name,filename)
    
def BrandLogoBluredImagePath(instance, filename):
    
    if ' ' in instance.en_name:
        name = instance.en_name.replace(' ','-')
        filename = filename.replace(' ','-')
    if '_' in instance.en_name:
        name = instance.en_name.replace('_','-')
        filename = filename.replace('_','-')
    else:
        name = instance.en_name
        filename = filename
    filename += 'Blured'
    return 'Brands/Images/{0}/{1}'.format(name,filename)  
    
def BrandLogoSecImagePath(instance, filename):
    
    if ' ' in instance.en_name:
        name = instance.en_name.replace(' ','-')
        filename = filename.replace(' ','-')
        filename = filename
    if '_' in instance.en_name:
        name = instance.en_name.replace('_','-')
        filename = filename.replace('_','-')
        filename = filename 
    else:
        name = instance.en_name
        filename = filename 
    filename = 'Sec' + filename
    return 'Brands/Images/{0}/{1}'.format(name,filename)

def BrandLogoSliderImagePath(instance, filename):
    
    if ' ' in instance.en_name:
        name = instance.en_name.replace(' ','-')
        filename = filename.replace(' ','-')
        filename = filename
    if '_' in instance.en_name:
        name = instance.en_name.replace('_','-')
        filename = filename.replace('_','-')
        filename = filename 
    else:
        name = instance.en_name
        filename = filename 
    filename = 'slider' + filename
    return 'Brands/Images/{0}/{1}'.format(name,filename)

class Brand(models.Model):
    fa_name = models.CharField(_( 'Persian Name' ), max_length=100)
    en_name = models.CharField(_( 'English Name' ), max_length=100)
    brief_explamations = models.TextField()
    descriptions = RichTextField(_( 'Description About Brand' ))
    country = models.CharField(max_length=100)
    logo_1th = models.ImageField(upload_to=BrandLogoImagePath)
    logo_blured = models.ImageField(upload_to=BrandLogoBluredImagePath, null=True, blank=True)
    logo_2th = models.ImageField(upload_to=BrandLogoSecImagePath, null=True, blank=True)
    logo_slider = models.ImageField(upload_to=BrandLogoSliderImagePath, null=True, blank=True)
    number_of_products = models.IntegerField(default=0)
    number_of_employees = models.IntegerField(default=0)
    founded_date = models.IntegerField(default=0)
    url = models.CharField(max_length=150)
    active = models.BooleanField(default=False)

    def __str__(self):
         return self.en_name