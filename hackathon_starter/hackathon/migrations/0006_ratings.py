# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hackathon', '0005_auto_20150627_1004'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating_ontime', models.IntegerField(default=b'-1')),
                ('rating_value', models.IntegerField(default=b'-1')),
                ('rating_reliability', models.IntegerField(default=b'-1')),
                ('rating_quality', models.IntegerField(default=b'-1')),
                ('merchant', models.ForeignKey(to='hackathon.Merchant')),
                ('user', models.ForeignKey(to='hackathon.User')),
            ],
        ),
    ]
