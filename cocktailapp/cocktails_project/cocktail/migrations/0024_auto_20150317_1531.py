# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('cocktail', '0023_userprofile_full_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advert',
            name='date_added',
            field=models.DateField(default=datetime.date(2015, 3, 17), auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date_added',
            field=models.DateField(default=datetime.date(2015, 3, 17), auto_now_add=True),
        ),
    ]
