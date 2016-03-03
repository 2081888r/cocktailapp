# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('cocktail', '0028_auto_20150322_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advert',
            name='date_added',
            field=models.DateField(default=datetime.date(2015, 3, 23), auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='cocktail',
            name='base',
            field=models.ForeignKey(blank=True, to='cocktail.CocktailBase', null=True),
        ),
        migrations.AlterField(
            model_name='cocktail',
            name='taste_palette',
            field=models.ForeignKey(blank=True, to='cocktail.CocktailTastePalette', null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date_added',
            field=models.DateField(default=datetime.date(2015, 3, 23), auto_now_add=True),
        ),
    ]
