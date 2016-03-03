# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cocktail', '0027_auto_20150322_0425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cocktail',
            name='name',
            field=models.CharField(default=b'', max_length=64),
        ),
    ]
