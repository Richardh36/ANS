# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0005_make_filter_spec_unique'),
        ('core', '0014_auto_20150502_1341'),
    ]

    operations = [
        migrations.AddField(
            model_name='productindexpage',
            name='intro',
            field=models.TextField(max_length=255, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='productindexpage',
            name='main_image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='wagtailimages.Image', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='productpage',
            name='intro',
            field=models.TextField(max_length=255, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='productpage',
            name='main_image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='wagtailimages.Image', blank=True, null=True),
            preserve_default=True,
        ),
    ]
