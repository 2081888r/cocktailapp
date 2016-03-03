# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cocktail', '0012_cocktail_ingredients'),
    ]

    operations = [
        migrations.CreateModel(
            name='TastePalette',
            fields=[
                ('ID', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=64)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameField(
            model_name='cocktail',
            old_name='user_id',
            new_name='bartender',
        ),
        migrations.RemoveField(
            model_name='cocktail',
            name='taste_pallet',
        ),
        migrations.AddField(
            model_name='cocktail',
            name='taste_palette',
            field=models.ForeignKey(default=1, to='cocktail.TastePalette'),
            preserve_default=False,
        ),
    ]
