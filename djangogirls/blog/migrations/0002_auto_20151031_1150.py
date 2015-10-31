# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='text',
            field=models.CharField(default=' ', max_length=5000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2015, 10, 31, 9, 50, 3, 711531, tzinfo=utc)),
        ),
    ]
