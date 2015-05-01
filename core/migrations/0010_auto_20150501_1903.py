# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_productindexpage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactpage',
            name='hero_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='wagtailimages.Image'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='homepage',
            name='hero_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='wagtailimages.Image'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='standardpage',
            name='hero_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='wagtailimages.Image'),
            preserve_default=True,
        ),
    ]
