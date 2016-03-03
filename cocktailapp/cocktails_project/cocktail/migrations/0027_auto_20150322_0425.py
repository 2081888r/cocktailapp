# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cocktail', '0026_auto_20150322_0335'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cocktail',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='cocktail',
            name='user_rated',
        ),
    ]
