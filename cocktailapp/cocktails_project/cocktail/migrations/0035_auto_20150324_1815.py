# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cocktail', '0034_bartenderratescocktail'),
    ]

    operations = [
        migrations.AddField(
            model_name='bartenderratescocktail',
            name='bartender',
            field=models.CharField(default=b'', max_length=64),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bartenderratescocktail',
            name='cocktail',
            field=models.CharField(default=b'', max_length=64),
            preserve_default=True,
        ),
    ]
