# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-09 07:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20160609_0635'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='name',
        ),
        migrations.AddField(
            model_name='candidate',
            name='fname',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='lname',
            field=models.CharField(max_length=255, null=True),
        ),
    ]