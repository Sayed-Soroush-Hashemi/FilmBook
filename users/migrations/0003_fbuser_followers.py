# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20150521_0807'),
    ]

    operations = [
        migrations.AddField(
            model_name='fbuser',
            name='followers',
            field=models.ManyToManyField(related_name='followers_rel_+', to='users.FBUser'),
        ),
    ]
