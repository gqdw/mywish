# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20150922_2338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mywish',
            name='price',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='mywish',
            name='project',
            field=models.ManyToManyField(to='main.Project', blank=True),
        ),
        migrations.AlterField(
            model_name='mywish',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]
