# Generated by Django 4.2.5 on 2023-10-02 09:08

from django.db import migrations, models
import django.db.models.deletion
import jdatetime
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('adminstrator', '0001_initial'),
        ('logs', '0003_categorylogs'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subsetlogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(default=uuid.uuid4)),
                ('status', models.CharField(max_length=255)),
                ('msg', models.CharField(blank=True, max_length=2550, null=True)),
                ('J_addition_datetime', models.CharField(default=jdatetime.datetime.now, max_length=15)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminstrator.adminlogin')),
            ],
        ),
    ]