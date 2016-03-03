# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('cocktail', '0016_auto_20150217_0553'),
    ]

    operations = [
        migrations.AddField(
            model_name='advert',
            name='advert_image',
            field=models.CharField(default=b'', max_length=256),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='advert',
            name='advert_title',
            field=models.CharField(default=b'', max_length=32),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='advert',
            name='brand_id',
            field=models.ForeignKey(default=1, to='cocktail.Brand'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='advert',
            name='date_added',
            field=models.DateField(default=datetime.date(2015, 2, 17), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='advert',
            name='date_to_expire',
            field=models.DateField(default=datetime.date(2015, 2, 17)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_title',
            field=models.CharField(default=b'', max_length=32),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='date_added',
            field=models.DateField(default=datetime.date(2015, 2, 17), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='brand',
            name='brand_name',
            field=models.CharField(default=b'', max_length=64),
        ),
    ]
