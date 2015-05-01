# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20150501_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='hero_text',
            field=models.TextField(max_length=255, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='homepage',
            name='hero_title',
            field=models.CharField(max_length=255, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='standardpage',
            name='intro',
            field=models.TextField(max_length=255, blank=True),
            preserve_default=True,
        ),
    ]
