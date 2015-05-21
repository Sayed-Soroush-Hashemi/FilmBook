# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='FBUser',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, serialize=False, primary_key=True, to=settings.AUTH_USER_MODEL)),
                ('nickname', models.CharField(max_length=100, null=True, blank=True)),
                ('birthday', models.DateField(null=True, blank=True)),
            ],
            options={
                'verbose_name': 'user',
                'abstract': False,
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
