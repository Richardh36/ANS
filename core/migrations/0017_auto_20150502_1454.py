# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_standardpage_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='productpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(template='core/blocks/heading.html')), ('paragraph', wagtail.wagtailcore.blocks.TextBlock(template='core/blocks/paragraph.html'))), blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='standardpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(template='core/blocks/heading.html')), ('paragraph', wagtail.wagtailcore.blocks.TextBlock(template='core/blocks/paragraph.html'))), blank=True),
            preserve_default=True,
        ),
    ]
