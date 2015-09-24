# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_mywish_begintime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='endtime',
            field=models.DateField(null=True, blank=True),
        ),
    ]
