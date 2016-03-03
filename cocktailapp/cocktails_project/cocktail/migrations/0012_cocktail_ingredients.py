# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cocktail', '0011_auto_20150217_0514'),
    ]

    operations = [
        migrations.AddField(
            model_name='cocktail',
            name='ingredients',
            field=models.CharField(default=b'', max_length=512),
            preserve_default=True,
        ),
    ]
