# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20150501_1903'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='hero_text',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='hero_title',
        ),
        migrations.AddField(
            model_name='homepage',
            name='intro',
            field=models.TextField(max_length=255, blank=True),
            preserve_default=True,
        ),
    ]
