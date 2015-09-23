# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_mywish_why'),
    ]

    operations = [
        migrations.AddField(
            model_name='mywish',
            name='begintime',
            field=models.DateField(default=datetime.datetime(2015, 9, 23, 5, 12, 40, 703948, tzinfo=utc), blank=True),
            preserve_default=False,
        ),
    ]
