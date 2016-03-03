# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cocktail', '0032_auto_20150324_1604'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cocktail',
            old_name='one_stars',
            new_name='one_star',
        ),
    ]
