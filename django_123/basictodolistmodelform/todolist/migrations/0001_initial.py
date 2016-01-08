# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('todo_text', models.CharField(max_length=250)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('priority', models.IntegerField(default=0)),
                ('difficulty', models.IntegerField(default=0)),
                ('done', models.BooleanField(default=False)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
            ],
        ),
    ]
