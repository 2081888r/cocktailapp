# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cocktail', '0013_auto_20150217_0522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cocktail',
            name='user_rated',
            field=models.SmallIntegerField(default=0),
        ),
    ]
