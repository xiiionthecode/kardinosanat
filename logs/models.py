from django.db import models
import uuid, os, jdatetime
from adminstrator.models import AdminLogin

class BlogLogs(models.Model):
    slug = models.SlugField(default=uuid.uuid4)
    author = models.ForeignKey(AdminLogin, on_delete=models.CASCADE)
    status = models.CharField(max_length=255)
    msg = models.CharField(max_length=2550, null=True, blank=True)
    J_addition_datetime = models.CharField(default=jdatetime.datetime.now, max_length=15)

class BrandLogs(models.Model):
    slug = models.SlugField(default=uuid.uuid4)
    author = models.ForeignKey(AdminLogin, on_delete=models.CASCADE)
    status = models.CharField(max_length=255)
    msg = models.CharField(max_length=2550, null=True, blank=True)
    J_addition_datetime = models.CharField(default=jdatetime.datetime.now, max_length=15)

class Categorylogs(models.Model):
    slug = models.SlugField(default=uuid.uuid4)
    author = models.ForeignKey(AdminLogin, on_delete=models.CASCADE)
    status = models.CharField(max_length=255)
    msg = models.CharField(max_length=2550, null=True, blank=True)
    J_addition_datetime = models.CharField(default=jdatetime.datetime.now, max_length=15)

class Subsetlogs(models.Model):
    slug = models.SlugField(default=uuid.uuid4)
    author = models.ForeignKey(AdminLogin, on_delete=models.CASCADE)
    status = models.CharField(max_length=255)
    msg = models.CharField(max_length=2550, null=True, blank=True)
    J_addition_datetime = models.CharField(default=jdatetime.datetime.now, max_length=15)