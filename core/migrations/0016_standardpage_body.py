# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20150502_1437'),
    ]

    operations = [
        migrations.AddField(
            model_name='standardpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock()), ('paragraph', wagtail.wagtailcore.blocks.TextBlock())), blank=True),
            preserve_default=True,
        ),
    ]
