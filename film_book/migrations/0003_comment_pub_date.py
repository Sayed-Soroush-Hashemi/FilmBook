# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('film_book', '0002_auto_20150521_0534'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 21, 7, 27, 16, 616895, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
