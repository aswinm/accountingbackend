# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_auto_20151031_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeduration',
            name='from_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='timeduration',
            name='to_time',
            field=models.DateTimeField(),
        ),
    ]
