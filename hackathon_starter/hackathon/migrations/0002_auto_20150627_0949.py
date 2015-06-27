# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hackathon', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='merchant',
            name='rating_ontime',
            field=models.IntegerField(default=b'-1'),
        ),
        migrations.AddField(
            model_name='merchant',
            name='rating_quality',
            field=models.IntegerField(default=b'-1'),
        ),
        migrations.AddField(
            model_name='merchant',
            name='rating_reliability',
            field=models.IntegerField(default=b'-1'),
        ),
        migrations.AddField(
            model_name='merchant',
            name='rating_value',
            field=models.IntegerField(default=b'-1'),
        ),
        migrations.AlterField(
            model_name='merchant',
            name='rating',
            field=models.IntegerField(default=b'-1'),
        ),
    ]
