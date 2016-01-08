# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import address.models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('First_name', models.CharField(max_length=200)),
                ('Last_name', models.CharField(max_length=200)),
                ('Sex', models.CharField(max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('Phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('Email', models.EmailField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
                ('Address', address.models.AddressField(to='address.Address')),
            ],
        ),
    ]
