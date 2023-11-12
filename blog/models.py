from django.db import models
from django.utils.translation import gettext as _
import uuid, os, jdatetime
from datetime import datetime
from ckeditor.fields import RichTextField 
from adminstrator.models import AdminLogin, AdminInfo


def BlogPosterPath(instance, filename):
    name = instance.title.replace(' ','-')
    filename = filename.replace(' ','-')
    return 'Blogs/Images/{0}/{1}'.format(name,filename)

class Blog(models.Model):
    slug = models.SlugField(default=uuid.uuid4)
    author = models.ForeignKey(AdminLogin, on_delete=models.CASCADE)
    author_info = models.ForeignKey(AdminInfo, on_delete=models.CASCADE)
    poster = models.ImageField(_('First Blog Poster'), upload_to=BlogPosterPath , null=True , blank=True)
    second_poster = models.ImageField(_('Second Blog Poster'), upload_to=BlogPosterPath , null=True , blank=True)
    title = models.CharField(_('Title of Post'), max_length=150)
    description = models.CharField(_('Description of Post'), max_length=10000)
    tags = models.CharField(_('Tags of Post'), max_length=500) #its need new app for tags
    article_text = RichTextField()
    J_addition_datetime = models.CharField(default=jdatetime.date.today, max_length=15)
    J_editition_datetime = models.CharField(default=jdatetime.date.today, max_length=15)
    day = models.CharField(max_length=20)
    month = models.CharField(max_length=50)
    year = models.CharField(max_length=50)
    url = models.CharField(max_length=150, unique=True)
    special_blog = models.BooleanField(_("its special ?"), default=False)
    active = models.BooleanField(_("Active ?"), default=True)
    view = models.IntegerField(default=0)
    readingtime = models.CharField(max_length=255, default='ذکر نشده است .')

    def __str__(self):
         return self.title


class BlogTag(models.Model):
    slug = models.SlugField(default=uuid.uuid4)
    name = models.CharField(max_length=50)
    numberOfUsed = models.IntegerField(default=1)
    numbOfClicked = models.IntegerField(default=0)
    active = models.BooleanField(default=True)

    def __str__(self):
         return self.name