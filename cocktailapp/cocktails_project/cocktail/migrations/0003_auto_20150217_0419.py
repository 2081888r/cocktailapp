# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('cocktail', '0002_brand_cocktail_comment_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advert',
            fields=[
                ('ID', models.AutoField(serialize=False, primary_key=True)),
                ('image', models.CharField(max_length=256)),
                ('date_added', models.DateField(auto_now_add=True)),
                ('date_to_expire', models.DateField()),
                ('brand_id', models.ForeignKey(to='cocktail.Brand')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameField(
            model_name='brand',
            old_name='id',
            new_name='ID',
        ),
        migrations.RenameField(
            model_name='cocktail',
            old_name='id',
            new_name='ID',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='id',
            new_name='ID',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='id',
            new_name='ID',
        ),
        migrations.RemoveField(
            model_name='cocktail',
            name='category',
        ),
        migrations.DeleteModel(
            name='CocktailCategory',
        ),
        migrations.AddField(
            model_name='brand',
            name='brand_name',
            field=models.CharField(default='', max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cocktail',
            name='how_to_make_comment',
            field=models.CharField(default='', max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cocktail',
            name='image',
            field=models.CharField(default='', max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cocktail',
            name='rating',
            field=models.SmallIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cocktail',
            name='taste_pallet',
            field=models.CharField(default='', max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cocktail',
            name='user_id',
            field=models.ForeignKey(default=0, to='cocktail.User'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cocktail',
            name='user_rated',
            field=models.CharField(default=0, max_length=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cocktail',
            name='views',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='cocktail_id',
            field=models.ForeignKey(default=0, to='cocktail.Cocktail'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_text',
            field=models.CharField(default='', max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='user_id',
            field=models.ForeignKey(default=0, to='cocktail.User'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='age_range',
            field=models.CharField(default='', max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(default='', max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default='', unique=True, max_length=75),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default='', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='sign_up_date',
            field=models.DateField(default=datetime.date(2015, 2, 17), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='time_last_used',
            field=models.DateTimeField(default=datetime.date(2015, 2, 17), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='workplace',
            field=models.CharField(default='', max_length=64),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cocktail',
            name='name',
            field=models.CharField(max_length=64),
        ),
    ]
