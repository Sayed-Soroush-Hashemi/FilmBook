# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_fbuser_followers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fbuser',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='images/users/'),
        ),
    ]
