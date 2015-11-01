# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20151027_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='client',
            field=models.ForeignKey(related_name='projects', to='clients.Client'),
        ),
    ]
