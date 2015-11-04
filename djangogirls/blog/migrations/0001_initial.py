# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('date_published', models.DateTimeField(default=datetime.datetime(2015, 11, 1, 17, 50, 55, 376668, tzinfo=utc))),
            ],
        ),
    ]
