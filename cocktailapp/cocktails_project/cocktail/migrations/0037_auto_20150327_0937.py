# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cocktail', '0036_auto_20150324_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cocktail',
            name='five_stars',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='cocktail',
            name='four_stars',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='cocktail',
            name='one_star',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='cocktail',
            name='three_stars',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='cocktail',
            name='two_stars',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
