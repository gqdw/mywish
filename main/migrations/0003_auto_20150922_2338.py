# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20150922_2309'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mywish',
            name='project',
        ),
        migrations.AddField(
            model_name='mywish',
            name='project',
            field=models.ManyToManyField(to='main.Project'),
        ),
    ]
