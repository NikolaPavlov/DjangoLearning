# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20151118_1247'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='publised_date',
            new_name='published_date',
        ),
    ]
