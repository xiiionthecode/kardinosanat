from django.db import models
from django.utils.translation import gettext as _
import uuid, os, jdatetime
from datetime import datetime
from ckeditor.fields import RichTextField 
from adminstrator.models import AdminLogin, AdminInfo
from brand.models import *
from category.models import *

class FeaturesCategories(models.Model):
    name = models.CharField(max_length=100)
    active=models.BooleanField(default=True)

    def __str__(self):
         return self.name


def ProductPosterImagePath(instance, filename):
    if ' ' in instance.enName:
        name = instance.enName.replace(' ','-')
        filename = 'Poster-'+filename.replace(' ','-')
    if '_' in instance.enName:
        name = instance.enName.replace('_','-')
        filename = 'Poster-'+filename.replace('_','-')
    else:
        name = instance.enName
        filename = 'Poster-'+filename

    return 'Products/Images/{0}/{1}'.format(name,filename)

class Product(models.Model):
    slug = models.SlugField(default=uuid.uuid4)
    Brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    ProductCategorySubset = models.ForeignKey(ProductCategorySubset, on_delete=models.CASCADE)
    faName = models.CharField(_( 'Persian Name' ), max_length=500)
    enName = models.CharField(_( 'English Name' ), max_length=500, null=True, blank=True)
    code = models.CharField(_( 'Reality Product CODE' ), max_length=200)
    poster = models.ImageField(upload_to=ProductPosterImagePath)
    J_addition_datetime = models.CharField(default=jdatetime.date.today, max_length=15)
    J_editition_datetime = models.CharField(default=jdatetime.date.today, max_length=15)
    review = RichTextField()
    tags = models.CharField(max_length=300)
    view = models.IntegerField(default=0)
    # like = models.IntegerField(default=0)
    # dislike = models.IntegerField(default=0)
    # numbOfComments = models.IntegerField(default=0)
    url = models.CharField(max_length=150)
    active = models.BooleanField(default=True)

    def __str__(self):
         return self.enName


class Feature(models.Model):
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    FeaturesCategories = models.ForeignKey(FeaturesCategories, on_delete=models.CASCADE)
    feature = models.CharField(max_length=100)
    descriptions = models.CharField(max_length=500)
    important = models.BooleanField(_('Important Features ?'), default=False)
    active=models.BooleanField(default=True)

    def __str__(self):
         return self.feature


def ProductOtherImagePath(instance, filename):

    if ' ' in instance.enName:
        name = instance.enName.replace(' ','-')
        filename = 'ProductImages-'+filename.replace(' ','-')
    if '_' in instance.enName:
        name = instance.enName.replace('_','-')
        filename = 'ProductImages-'+filename.replace('_','-')
    else:
        name = instance.enName
        filename = 'ProductImages-'+filename

    return 'Products/Images/{0}/{1}'.format(name,filename)

class ProductImage(models.Model):
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    enName = models.CharField(_( 'English Name' ), max_length=500)
    image = models.ImageField(upload_to=ProductOtherImagePath)
    active = models.BooleanField(default=True)
    
    def __str__(self):
         return self.enName


class ProductTag(models.Model):
    slug = models.SlugField(default=uuid.uuid4)
    name = models.CharField(max_length=50)
    numberOfUsed = models.IntegerField(default=1)
    numbOfClicked = models.IntegerField(default=0)
    active = models.BooleanField(default=True)

    def __str__(self):
         return self.name