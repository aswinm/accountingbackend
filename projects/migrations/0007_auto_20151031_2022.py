# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_auto_20151031_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeduration',
            name='duration',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='timeduration',
            name='from_time',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='timeduration',
            name='project',
            field=models.ForeignKey(related_name='time_durations', to='projects.Project'),
        ),
        migrations.AlterField(
            model_name='timeduration',
            name='to_time',
            field=models.CharField(max_length=255),
        ),
    ]
