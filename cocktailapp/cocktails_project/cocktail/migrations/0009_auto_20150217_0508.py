# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cocktail', '0008_auto_20150217_0504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cocktail',
            name='how_to_make_comment',
            field=models.CharField(default=b'', max_length=256),
        ),
        migrations.AlterField(
            model_name='cocktail',
            name='image',
            field=models.CharField(default=b'', max_length=256),
        ),
        migrations.AlterField(
            model_name='cocktail',
            name='name',
            field=models.CharField(default=b'', max_length=64),
        ),
        migrations.AlterField(
            model_name='cocktail',
            name='rating',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cocktail',
            name='user_id',
            field=models.ForeignKey(to='cocktail.Bartender'),
        ),
        migrations.AlterField(
            model_name='cocktail',
            name='user_rated',
            field=models.CharField(default=b'', max_length=256),
        ),
    ]
