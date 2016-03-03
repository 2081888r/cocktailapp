# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cocktail', '0007_auto_20150217_0500'),
    ]

    operations = [
        migrations.AddField(
            model_name='cocktail',
            name='how_to_make_comment',
            field=models.CharField(default='', max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cocktail',
            name='user_id',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cocktail',
            name='user_rated',
            field=models.CharField(default='', max_length=2000),
            preserve_default=False,
        ),
    ]
