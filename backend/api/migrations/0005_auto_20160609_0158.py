# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-09 01:58
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20160609_0156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jd',
            name='max_experience',
            field=models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(58)]),
        ),
        migrations.AlterField(
            model_name='jd',
            name='max_salary',
            field=models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(58)]),
        ),
        migrations.AlterField(
            model_name='jd',
            name='min_experience',
            field=models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(58)]),
        ),
        migrations.AlterField(
            model_name='jd',
            name='min_salary',
            field=models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(58)]),
        ),
    ]
