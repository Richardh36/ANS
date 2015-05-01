# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20150501_1904'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactpage',
            name='intro',
            field=models.TextField(blank=True, max_length=255),
            preserve_default=True,
        ),
    ]
