# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-09 19:27
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_studentinstance'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentinstance',
            name='attend_time',
            field=models.TimeField(default=datetime.datetime(2017, 12, 9, 19, 27, 50, 827175, tzinfo=utc), verbose_name='출책 시간'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentinstance',
            name='status',
            field=models.CharField(choices=[('a', 'Attend'), ('n', 'Absance'), ('l', 'Late')], default='l', max_length=1),
            preserve_default=False,
        ),
    ]
