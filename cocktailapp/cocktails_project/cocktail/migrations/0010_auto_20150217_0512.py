# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('cocktail', '0009_auto_20150217_0508'),
    ]

    operations = [
        migrations.AddField(
            model_name='bartender',
            name='age_range',
            field=models.CharField(default=b'', max_length=5),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bartender',
            name='city',
            field=models.CharField(default=b'', max_length=64),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bartender',
            name='sign_up_date',
            field=models.DateField(default=datetime.date(2015, 2, 17), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bartender',
            name='time_last_used',
            field=models.DateTimeField(default=datetime.date(2015, 2, 17), auto_now=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bartender',
            name='workplace',
            field=models.CharField(default=b'', max_length=64),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bartender',
            name='email',
            field=models.EmailField(default=b'', unique=True, max_length=75),
        ),
        migrations.AlterField(
            model_name='bartender',
            name='name',
            field=models.CharField(default=b'', max_length=128),
        ),
    ]
