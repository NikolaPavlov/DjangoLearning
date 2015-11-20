# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
        ('twetts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Twett',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('text', models.CharField(max_length=160)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('country', models.CharField(max_length=30)),
                ('is_active', models.BooleanField(default=True)),
                ('user', models.ForeignKey(to='user_profile.User')),
            ],
        ),
        migrations.RemoveField(
            model_name='tweet',
            name='user',
        ),
        migrations.DeleteModel(
            name='Tweet',
        ),
    ]
