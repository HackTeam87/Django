# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-11 02:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_auto_20170611_0415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/med/', verbose_name='Ваше фото'),
        ),
    ]
