# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0005_make_filter_spec_unique'),
        ('core', '0004_auto_20150501_1528'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='hero_image',
            field=models.ForeignKey(to='wagtailimages.Image', null=True, on_delete=django.db.models.deletion.SET_NULL),
            preserve_default=True,
        ),
    ]
