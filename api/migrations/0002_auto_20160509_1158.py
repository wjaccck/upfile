# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recode_dirs',
            name='sub_file',
        ),
        migrations.AlterField(
            model_name='up_file',
            name='base_dir',
            field=models.ForeignKey(related_name='base_file_dir', to='api.Recode_dirs'),
        ),
    ]
