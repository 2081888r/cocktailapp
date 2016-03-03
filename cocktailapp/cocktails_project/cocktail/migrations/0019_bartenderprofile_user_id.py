# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cocktail', '0018_auto_20150316_1558'),
    ]

    operations = [
        migrations.AddField(
            model_name='bartenderprofile',
            name='user_id',
            field=models.OneToOneField(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
