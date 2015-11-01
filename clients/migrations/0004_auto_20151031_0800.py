# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0003_auto_20151027_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='no_of_projects',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='total_income',
            field=models.FloatField(default=0, null=True, blank=True),
        ),
    ]
