# Generated by Django 4.2.5 on 2023-09-20 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_view'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='url',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
