# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20150503_1340'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productpage',
            name='listing_image',
        ),
        migrations.RemoveField(
            model_name='productpage',
            name='listing_summary',
        ),
    ]
