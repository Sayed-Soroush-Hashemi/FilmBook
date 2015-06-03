# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20150602_1856'),
    ]

    operations = [
        migrations.AddField(
            model_name='fbuser',
            name='lastget',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 1, 0, 0, tzinfo=utc)),
        ),
    ]
