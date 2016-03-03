# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('cocktail', '0025_auto_20150319_1641'),
    ]

    operations = [
        migrations.AddField(
            model_name='cocktail',
            name='slug',
            field=models.SlugField(default=b'', unique=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='advert',
            name='date_added',
            field=models.DateField(default=datetime.date(2015, 3, 22), auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='cocktail',
            name='name',
            field=models.CharField(default=b'', unique=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date_added',
            field=models.DateField(default=datetime.date(2015, 3, 22), auto_now_add=True),
        ),
    ]
