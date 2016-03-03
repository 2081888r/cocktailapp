# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cocktail', '0010_auto_20150217_0512'),
    ]

    operations = [
        migrations.AddField(
            model_name='cocktail',
            name='taste_pallet',
            field=models.CharField(default=0, max_length=64),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cocktail',
            name='views',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
