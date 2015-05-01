# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_contactpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='hero_text',
            field=models.TextField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='homepage',
            name='hero_title',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
