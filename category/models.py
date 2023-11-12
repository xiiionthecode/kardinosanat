from django.db import models
import uuid, os 

def CategoryVectorImagePath(instance, filename):
    
    if ' ' in instance.name:
        name = instance.url.replace(' ','-')
        filename = filename.replace(' ','-')
    if '_' in instance.name:
        name = instance.url.replace('_','-')
        filename = filename.replace('_','-')
    else:
        name = instance.url
        filename = filename

    return 'Category/Images/{0}/{1}'.format(name,filename)
   

class ProductCategory(models.Model):
    slug = models.SlugField(default=uuid.uuid4)
    name = models.CharField(max_length=100)
    vector = models.ImageField(upload_to=CategoryVectorImagePath)
    position = models.IntegerField()
    number_of_products = models.IntegerField()
    url = models.CharField(max_length=150)
    active = models.BooleanField(default=True)

    def __str__(self):
         return self.name



def SubsetVectorImagePath(instance, filename):
    
    if ' ' in instance.name:
        name = instance.name.replace(' ','-')
        filename = filename.replace(' ','-')
    if '_' in instance.name:
        name = instance.name.replace('_','-')
        filename = filename.replace('_','-')
    else:
        name = instance.name
        filename = filename

    return 'Category/Subset/Images/{0}/{1}'.format(name,filename)

class ProductCategorySubset(models.Model):
    slug = models.SlugField(default=uuid.uuid4)
    ProductCategory = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, null=True, blank=True)
    ref_slug = models.SlugField()
    name = models.CharField(max_length=100)
    vector = models.ImageField(upload_to=SubsetVectorImagePath)
    subset_number = models.IntegerField()
    position = models.IntegerField()
    number_of_products = models.IntegerField()
    url = models.CharField(max_length=150)
    active = models.BooleanField(default=True)

    def __str__(self):
         return self.name