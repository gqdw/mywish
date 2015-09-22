# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyWish',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('url', models.URLField()),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('begintime', models.DateField(auto_now=True)),
                ('endtime', models.DateField()),
                ('todo', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='mywish',
            name='project',
            field=models.ForeignKey(to='main.Project'),
        ),
    ]
