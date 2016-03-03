# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cocktail', '0003_auto_20150217_0419'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advert',
            name='ID',
        ),
        migrations.RemoveField(
            model_name='brand',
            name='ID',
        ),
        migrations.RemoveField(
            model_name='cocktail',
            name='ID',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='ID',
        ),
        migrations.RemoveField(
            model_name='user',
            name='ID',
        ),
        migrations.RemoveField(
            model_name='user',
            name='age_range',
        ),
        migrations.RemoveField(
            model_name='user',
            name='city',
        ),
        migrations.RemoveField(
            model_name='user',
            name='sign_up_date',
        ),
        migrations.RemoveField(
            model_name='user',
            name='time_last_used',
        ),
        migrations.RemoveField(
            model_name='user',
            name='workplace',
        ),
        migrations.AddField(
            model_name='advert',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=0, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='brand',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=0, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cocktail',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=0, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=0, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=0, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
