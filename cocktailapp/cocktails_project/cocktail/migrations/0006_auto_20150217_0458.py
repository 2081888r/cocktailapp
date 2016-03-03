# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cocktail', '0005_auto_20150217_0456'),
    ]

    operations = [
        migrations.AddField(
            model_name='cocktail',
            name='image',
            field=models.CharField(default='', max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cocktail',
            name='rating',
            field=models.SmallIntegerField(default=0),
            preserve_default=False,
        ),
    ]
