# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20151031_0701'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='total_duration_num',
            field=models.IntegerField(default=0),
        ),
    ]
