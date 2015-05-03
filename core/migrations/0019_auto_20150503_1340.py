# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_auto_20150502_1457'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactpage',
            name='company_name',
            field=models.CharField(max_length=100, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactpage',
            name='country',
            field=models.CharField(max_length=50, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactpage',
            name='county',
            field=models.CharField(max_length=50, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactpage',
            name='line1',
            field=models.CharField(verbose_name='First line', max_length=50, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactpage',
            name='line2',
            field=models.CharField(verbose_name='Second line', blank=True, max_length=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contactpage',
            name='postcode',
            field=models.CharField(max_length=10, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactpage',
            name='town',
            field=models.CharField(max_length=50, default=''),
            preserve_default=False,
        ),
    ]
