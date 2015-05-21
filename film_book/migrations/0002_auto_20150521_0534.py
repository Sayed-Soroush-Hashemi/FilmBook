# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('film_book', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rate',
            name='user',
            field=models.ForeignKey(to='users.FBUser'),
        ),
        migrations.AddField(
            model_name='post',
            name='movie',
            field=models.ForeignKey(to='film_book.Movie'),
        ),
        migrations.AddField(
            model_name='post',
            name='poster',
            field=models.ForeignKey(to='users.FBUser'),
        ),
        migrations.AddField(
            model_name='post',
            name='rate',
            field=models.ForeignKey(to='film_book.Rate'),
        ),
        migrations.AddField(
            model_name='comment',
            name='commenter',
            field=models.ForeignKey(to='users.FBUser'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(to='film_book.Post'),
        ),
    ]
