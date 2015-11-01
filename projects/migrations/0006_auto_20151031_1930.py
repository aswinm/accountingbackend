# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_project_total_duration_num'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeDuration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('from_time', models.DateTimeField()),
                ('to_time', models.DateTimeField()),
                ('duration', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='project',
            name='total_duration',
            field=models.CharField(default=b'', max_length=255),
        ),
        migrations.AddField(
            model_name='timeduration',
            name='project',
            field=models.ForeignKey(to='projects.Project'),
        ),
    ]
