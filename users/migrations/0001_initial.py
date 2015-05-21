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
                ('user_ptr', models.OneToOneField(auto_created=True, primary_key=True, serialize=False, parent_link=True, to=settings.AUTH_USER_MODEL)),
                ('nickname', models.CharField(blank=True, max_length=100, null=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, upload_to='users/images', null=True)),
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
