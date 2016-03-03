# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cocktail', '0014_auto_20150217_0526'),
    ]

    operations = [
        migrations.CreateModel(
            name='CocktailBase',
            fields=[
                ('ID', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=64)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameModel(
            old_name='TastePalette',
            new_name='CocktailTastePalette',
        ),
        migrations.AddField(
            model_name='cocktail',
            name='base',
            field=models.ForeignKey(default=1, to='cocktail.CocktailBase'),
            preserve_default=False,
        ),
    ]
