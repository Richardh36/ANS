# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_productpage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactpage',
            old_name='hero_image',
            new_name='main_image',
        ),
        migrations.RenameField(
            model_name='homepage',
            old_name='hero_image',
            new_name='main_image',
        ),
        migrations.RenameField(
            model_name='standardpage',
            old_name='hero_image',
            new_name='main_image',
        ),
    ]
