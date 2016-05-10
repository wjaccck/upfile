# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20160509_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='up_file',
            name='base_dir',
            field=models.ForeignKey(related_name='base_file_dir', to='api.Dirs'),
        ),
        migrations.AlterField(
            model_name='up_file',
            name='file_name',
            field=models.CharField(max_length=100, db_index=True),
        ),
        migrations.DeleteModel(
            name='Files',
        ),
    ]
