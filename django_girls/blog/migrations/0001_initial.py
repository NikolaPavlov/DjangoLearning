# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=datetime.datetime(2015, 11, 18, 10, 45, 1, 300258, tzinfo=utc))),
                ('publised_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
