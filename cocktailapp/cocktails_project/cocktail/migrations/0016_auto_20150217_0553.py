# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cocktail', '0015_auto_20150217_0534'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='cocktail_id',
            field=models.ForeignKey(default=1, to='cocktail.Cocktail'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='user_id',
            field=models.ForeignKey(default=1, to='cocktail.Bartender'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_text',
            field=models.CharField(default=b'', max_length=256),
        ),
    ]
