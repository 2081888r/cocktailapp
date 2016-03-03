# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cocktail', '0004_auto_20150217_0451'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advert',
            name='brand_id',
        ),
        migrations.RemoveField(
            model_name='advert',
            name='date_added',
        ),
        migrations.RemoveField(
            model_name='advert',
            name='date_to_expire',
        ),
        migrations.RemoveField(
            model_name='advert',
            name='id',
        ),
        migrations.RemoveField(
            model_name='advert',
            name='image',
        ),
        migrations.RemoveField(
            model_name='brand',
            name='id',
        ),
        migrations.RemoveField(
            model_name='cocktail',
            name='how_to_make_comment',
        ),
        migrations.RemoveField(
            model_name='cocktail',
            name='id',
        ),
        migrations.RemoveField(
            model_name='cocktail',
            name='image',
        ),
        migrations.RemoveField(
            model_name='cocktail',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='cocktail',
            name='taste_pallet',
        ),
        migrations.RemoveField(
            model_name='cocktail',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='cocktail',
            name='user_rated',
        ),
        migrations.RemoveField(
            model_name='cocktail',
            name='views',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='cocktail_id',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='id',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='user',
            name='id',
        ),
        migrations.AddField(
            model_name='advert',
            name='ID',
            field=models.AutoField(default=0, serialize=False, primary_key=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='brand',
            name='ID',
            field=models.AutoField(default=0, serialize=False, primary_key=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cocktail',
            name='ID',
            field=models.AutoField(default=0, serialize=False, primary_key=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='ID',
            field=models.AutoField(default=0, serialize=False, primary_key=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='ID',
            field=models.AutoField(default=0, serialize=False, primary_key=True),
            preserve_default=False,
        ),
    ]
