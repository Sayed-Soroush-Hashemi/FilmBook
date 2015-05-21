# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.auth.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='FBUser',
            fields=[
                ('user_ptr', models.OneToOneField(serialize=False, to=settings.AUTH_USER_MODEL, auto_created=True, primary_key=True, parent_link=True)),
                ('nickname', models.CharField(max_length=100, blank=True, null=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('image', models.FileField(blank=True, upload_to='users/images', null=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
