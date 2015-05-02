# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0005_make_filter_spec_unique'),
        ('core', '0017_auto_20150502_1454'),
    ]

    operations = [
        migrations.AddField(
            model_name='productpage',
            name='listing_image',
            field=models.ForeignKey(blank=True, related_name='+', null=True, on_delete=django.db.models.deletion.SET_NULL, to='wagtailimages.Image'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='productpage',
            name='listing_summary',
            field=models.TextField(max_length=255, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contactpage',
            name='main_image',
            field=models.ForeignKey(blank=True, related_name='+', null=True, on_delete=django.db.models.deletion.SET_NULL, to='wagtailimages.Image'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='homepage',
            name='main_image',
            field=models.ForeignKey(blank=True, related_name='+', null=True, on_delete=django.db.models.deletion.SET_NULL, to='wagtailimages.Image'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='productindexpage',
            name='main_image',
            field=models.ForeignKey(blank=True, related_name='+', null=True, on_delete=django.db.models.deletion.SET_NULL, to='wagtailimages.Image'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='productpage',
            name='main_image',
            field=models.ForeignKey(blank=True, related_name='+', null=True, on_delete=django.db.models.deletion.SET_NULL, to='wagtailimages.Image'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='standardpage',
            name='main_image',
            field=models.ForeignKey(blank=True, related_name='+', null=True, on_delete=django.db.models.deletion.SET_NULL, to='wagtailimages.Image'),
            preserve_default=True,
        ),
    ]
