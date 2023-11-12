# Generated by Django 4.2.5 on 2023-10-14 09:36

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import jdatetime
import product.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('brand', '0002_rename_briefexplamations_brand_brief_explamations_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeaturesCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(default=uuid.uuid4)),
                ('faName', models.CharField(max_length=500, verbose_name='Persian Name')),
                ('enName', models.CharField(blank=True, max_length=500, null=True, verbose_name='English Name')),
                ('code', models.CharField(max_length=200, verbose_name='Reality Product CODE')),
                ('poster', models.ImageField(upload_to=product.models.ProductPosterImagePath)),
                ('J_addition_datetime', models.CharField(default=jdatetime.date.today, max_length=15)),
                ('J_editition_datetime', models.CharField(default=jdatetime.date.today, max_length=15)),
                ('review', ckeditor.fields.RichTextField()),
                ('tags', models.CharField(max_length=300)),
                ('view', models.IntegerField(default=0)),
                ('url', models.CharField(max_length=150)),
                ('active', models.BooleanField(default=True)),
                ('Brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brand.brand')),
                ('FeaturesCategories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.featurescategories')),
            ],
        ),
        migrations.CreateModel(
            name='ProductTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(default=uuid.uuid4)),
                ('name', models.CharField(max_length=50)),
                ('numberOfUsed', models.IntegerField(default=1)),
                ('numbOfClicked', models.IntegerField(default=0)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enName', models.CharField(max_length=500, verbose_name='English Name')),
                ('image', models.ImageField(upload_to=product.models.ProductOtherImagePath)),
                ('active', models.BooleanField(default=True)),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature', models.CharField(max_length=100)),
                ('descriptions', models.CharField(max_length=500)),
                ('important', models.BooleanField(default=False, verbose_name='Important Features ?')),
                ('active', models.BooleanField(default=True)),
                ('FeaturesCategories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.featurescategories')),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
    ]
