# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='API',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('api_name', models.CharField(max_length=30)),
                ('api_version', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('request_type', models.CharField(max_length=10, choices=[(b'get', b'GET Request'), (b'post', b'POST Request')])),
                ('request_body', models.CharField(max_length=180)),
            ],
        ),
        migrations.AddField(
            model_name='api',
            name='transaction',
            field=models.ForeignKey(related_name='transactions', blank=True, to='gringotts.Transaction', null=True),
        ),
    ]
