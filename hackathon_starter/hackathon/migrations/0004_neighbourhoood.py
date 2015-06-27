# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hackathon', '0003_area'),
    ]

    operations = [
        migrations.CreateModel(
            name='Neighbourhoood',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'Parktown', max_length=140)),
                ('area', models.ForeignKey(to='hackathon.Area')),
            ],
        ),
    ]
