# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20160509_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dirs',
            name='name',
            field=models.CharField(unique=True, max_length=100),
        ),
    ]
