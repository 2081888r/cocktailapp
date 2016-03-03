# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cocktail', '0019_bartenderprofile_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('workplace', models.CharField(default=b'', max_length=64)),
                ('fav_cocktail', models.CharField(default=b'', max_length=64)),
                ('avatar', models.ImageField(upload_to=b'bartender_images', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='bartenderprofile',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='BartenderProfile',
        ),
    ]
