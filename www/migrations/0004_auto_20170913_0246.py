# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-13 01:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0003_auto_20170913_0225'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='bio',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='birthday',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='person',
            name='github',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='responsibilties',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='person',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=40),
        ),
    ]