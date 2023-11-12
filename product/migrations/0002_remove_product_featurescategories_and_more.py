# Generated by Django 4.2.5 on 2023-10-15 07:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_productcategorysubset_ref_slug'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='FeaturesCategories',
        ),
        migrations.AddField(
            model_name='product',
            name='ProductCategorySubset',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='category.productcategorysubset'),
            preserve_default=False,
        ),
    ]
