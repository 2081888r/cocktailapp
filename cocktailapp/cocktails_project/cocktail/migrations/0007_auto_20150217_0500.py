# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cocktail', '0006_auto_20150217_0458'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bartender',
            fields=[
                ('ID', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('email', models.EmailField(unique=True, max_length=75)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
