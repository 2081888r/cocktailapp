# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cocktail', '0021_auto_20150316_2122'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='user_id',
            new_name='user',
        ),
    ]
