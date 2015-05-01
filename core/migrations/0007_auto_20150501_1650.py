# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0005_make_filter_spec_unique'),
        ('core', '0006_standardpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactpage',
            name='hero_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wagtailimages.Image'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='standardpage',
            name='hero_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wagtailimages.Image'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='standardpage',
            name='intro',
            field=models.TextField(max_length=255, default=''),
            preserve_default=False,
        ),
    ]
