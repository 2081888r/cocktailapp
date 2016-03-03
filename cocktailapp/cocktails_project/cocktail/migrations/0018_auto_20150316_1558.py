# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('cocktail', '0017_auto_20150217_0600'),
    ]

    operations = [
        migrations.CreateModel(
            name='BartenderProfile',
            fields=[
                ('ID', models.AutoField(serialize=False, primary_key=True)),
                ('fav_cocktail', models.CharField(default=b'', max_length=64)),
                ('workplace', models.CharField(default=b'', max_length=64)),
                ('avatar', models.ImageField(upload_to=b'bartender_images', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='advert',
            name='date_added',
            field=models.DateField(default=datetime.date(2015, 3, 16), auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='cocktail',
            name='bartender',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date_added',
            field=models.DateField(default=datetime.date(2015, 3, 16), auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user_id',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Bartender',
        ),
    ]
