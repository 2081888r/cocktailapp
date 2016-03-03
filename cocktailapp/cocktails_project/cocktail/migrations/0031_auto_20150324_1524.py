# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cocktail', '0030_auto_20150324_1521'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advert',
            name='brand_id',
        ),
        migrations.DeleteModel(
            name='Advert',
        ),
        migrations.DeleteModel(
            name='Brand',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='cocktail_id',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
