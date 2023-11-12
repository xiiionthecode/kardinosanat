from django.db import models
from django.utils.translation import gettext as _
import uuid

class GenderChoices(models.IntegerChoices):
    null = 0 ,
    male = 1 ,
    female = 2 , 
    whatyouneed = 3 ,

class AdminLogin(models.Model):
    slug = models.SlugField(default=uuid.uuid4)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)
    mail = models.EmailField()
    phonenumber = models.CharField(max_length=12, unique=True)
    joined_at = models.CharField(max_length=30)
    modified_at = models.CharField(max_length=30, null=True , blank=True)
    lastlogin = models.CharField(max_length=30)

class AdminInfo(models.Model):
    slug = models.SlugField(default=uuid.uuid4)
    AdminLogin = models.ForeignKey(AdminLogin, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    age = models.CharField(max_length=4)
    gender = models.IntegerField(default=GenderChoices.null, choices=GenderChoices.choices)
    birthday_date = models.CharField(max_length=30)
    complited_at = models.CharField(max_length=30)



    