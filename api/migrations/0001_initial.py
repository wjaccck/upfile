# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Azure_key',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sig', models.CharField(max_length=300)),
                ('name', models.CharField(max_length=300)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Dirs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Recode_dirs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('base_dir', models.ForeignKey(related_name='base_dir', to='api.Dirs')),
                ('sub_dir', models.ManyToManyField(related_name='sub_dir', to='api.Dirs')),
                ('sub_file', models.ManyToManyField(to='api.Files')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(max_length=100)),
                ('alias', models.CharField(max_length=100)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Up_file',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('blob_name', models.CharField(max_length=100, db_index=True)),
                ('blob_url', models.URLField(blank=True)),
                ('file_md5', models.CharField(default='', max_length=100, blank=True)),
                ('file_location', models.CharField(max_length=300)),
                ('department', models.CharField(default='emoney', max_length=100, db_index=True)),
                ('desc', models.TextField(blank=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('base_dir', models.ForeignKey(to='api.Recode_dirs')),
                ('file_name', models.ForeignKey(to='api.Files')),
                ('status', models.ForeignKey(to='api.Status')),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
    ]
