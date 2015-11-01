# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20151027_1727'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='total_time_duration',
            new_name='total_duration',
        ),
    ]
