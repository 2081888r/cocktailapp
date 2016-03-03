# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cocktail', '0031_auto_20150324_1524'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cocktail',
            old_name='rating',
            new_name='five_stars',
        ),
        migrations.AddField(
            model_name='cocktail',
            name='four_stars',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cocktail',
            name='one_stars',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cocktail',
            name='three_stars',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cocktail',
            name='two_stars',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
