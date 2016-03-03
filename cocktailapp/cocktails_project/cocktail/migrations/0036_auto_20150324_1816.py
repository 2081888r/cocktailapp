# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('cocktail', '0035_auto_20150324_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bartenderratescocktail',
            name='bartender',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='bartenderratescocktail',
            name='cocktail',
            field=models.ForeignKey(to='cocktail.Cocktail'),
        ),
    ]
