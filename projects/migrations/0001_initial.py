# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0003_auto_20151027_1706'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('total_cost', models.FloatField()),
                ('total_time_duration', models.CharField(max_length=255)),
                ('client', models.ForeignKey(to='clients.Client')),
            ],
        ),
    ]
