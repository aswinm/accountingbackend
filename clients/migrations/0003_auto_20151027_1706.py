# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_remove_client_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='no_of_projects',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='client',
            name='total_income',
            field=models.FloatField(default=0),
        ),
    ]
